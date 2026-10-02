default(parisizemax,1600000000);
default(parisize,128000000);
polys=[x^2+83,x^6+243*x^4+2*x^3+20676*x^2-504*x+613869,x^18+729*x^16+239175*x^14+46336113*x^12+5840207892*x^10+2*x^9+496545240618*x^8-5994*x^7+28474853493801*x^6+1767456*x^5+1061984381299947*x^4-100445166*x^3+23373938989409508*x^2+928169928*x+231328546685761389];
expected=[3,63,10774323];
{
for(n=1,3,
  print("BEGIN_LAYER ",n-1);
  b=bnfinit(polys[n],1);
  if(b.no!=expected[n] || b.cyc!=[expected[n]],error("class group mismatch"));
  P=idealprimedec(b,3);
  if(#P!=2,error("prime count mismatch"));
  coords=vector(2,j,bnfisprincipal(b,P[j],0));
  orders=vector(2,j,b.no/gcd(b.no,coords[j][1]));
  if(orders!=vector(2,j,3^n),error("prime-class orders mismatch"));
  print("CLGP=",b.clgp," SIGN=",b.sign," P_EF=",vector(2,j,[P[j].e,P[j].f])," COORD=",coords," ORDER=",orders);
  logcl=bnflog(b,3);
  if(logcl!=[[],[],[]],error("logarithmic class mismatch"));
  print("LOGCL=",logcl);
  if(n==2,
    emb=nfisincl(y^2+83,b.pol)[1];
    J=idealadd(b,7,lift(emb)-1);
    if(idealnorm(b,J)==1,error("lifted nonprincipal prime became unit ideal"));
    principal=bnfisprincipal(b,J,0);
    print("LIFTED_P7_NORM=",idealnorm(b,J)," LIFTED_P7_CLASS=",principal);
    if(principal==[0]~,error("expected independently observed noncapitulation"));
    print("ORIGINAL_CAPITULATION_ASSERTION_DISPROVED");
  );
  comp=polcompositum(x^2+83,polsubcyclo(3^(n+1),3^(n-1)))[1];
  if(nfisisom(comp,b.pol)==0,error("cyclotomic field identity mismatch"));
  print("CYCLOTOMIC_LAYER_IDENTITY_OK");
  if(n<3,cert=bnfcertify(b);if(cert!=1,error("certification failed"));print("CERTIFIED=",cert),print("K2_GRH_CONDITIONAL=true"));
);
print("REPLAY_CLASS_DATA_OK");
}
quit;
