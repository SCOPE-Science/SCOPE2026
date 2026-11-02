// Standalone stationary-fluctuation cross-check for two covariance-matched propulsion laws.
#include <cmath>
#include <cstdio>
#include <cstdint>
#include <random>
#include <vector>
#include <algorithm>
struct Stats {double mean,variance;};
Stats simulate(int model,double k,double g,double v,int N,double T,uint64_t seed){
 std::mt19937_64 rg(seed);
 std::uniform_real_distribution<double> uni(0.,1.);
 std::vector<double> w(N);
 for(int i=0;i<N;++i){
   double x=0., work=0., t=-40./k; int state;
   if(model==3){ double z=uni(rg); state=(z<.5?0:(z<.75?1:-1));}
   else state=uni(rg)<.5?1:-1;
   while(t<T){
     const double rate=model==3?g:g/2.;
     double dt=-std::log(std::max(1.e-300,uni(rg)))/rate;
     if(t+dt>T) dt=T-t;
     const double u=(model==3?v*state:v*state/std::sqrt(2.0));
     const double new_x=u/k+(x-u/k)*std::exp(-k*dt);
     if(t>=0.) work+=u*(new_x-x);
     else if(t+dt>0.){
       const double at0=u/k+(x-u/k)*std::exp(k*t); // t<0
       work+=u*(new_x-at0);
     }
     x=new_x;t+=dt;
     if(t>=T)break;
     if(model==2) state=-state;
     else if(state) state=0;
     else state=uni(rg)<.5?1:-1;
   }
   w[i]=work;
 }
 double mu=0.,ss=0.;
 for(double z:w)mu+=z;mu/=N;
 for(double z:w)ss+=(z-mu)*(z-mu);
 return {mu/T,ss/(N-1)/T};
}
int main(){
 for(double g:{0.35,1.0,3.0})for(int model:{2,3}){
  const double k=1.,v=1.4;
  Stats x=simulate(model,k,g,v,50000,250.,1000+(int)(100*g)+model);
  double pred=model==3?g*std::pow(v,4)/(4*std::pow(k+g,2)):g*k*std::pow(v,4)/(2*std::pow(k+g,3));
  double mean= g*v*v/(2*(k+g));
  printf("g=%.2f model=%d mean %.8g predicted %.8g variance %.8g predicted %.8g relative_error %.3g\n",g,model,x.mean,mean,x.variance,pred,x.variance/pred-1.);
 }
}
