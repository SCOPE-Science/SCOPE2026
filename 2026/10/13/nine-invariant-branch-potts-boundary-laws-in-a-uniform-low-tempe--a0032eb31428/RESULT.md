# Nine invariant-branch Potts boundary laws in a uniform low-temperature regime
## Finding
Consider the three-state ferromagnetic Potts model on a Cayley tree of integer order \(k\ge4\), with \(\theta=\exp(J\beta)>1\). In the two-value boundary construction of Rahmatullaev and Dekhkonov, fix
\[
M=\begin{pmatrix}k&0\\1&k-1\end{pmatrix}
\]
and restrict to their invariant set \(I_1=\{h_2=l_2=0\}\). With
\[
f_\theta(x)=\log\frac{\theta e^x+2}{\theta+e^x+1},
\]
the reduced equations are
\[
h=kf_\theta(h),\qquad l=f_\theta(h)+(k-1)f_\theta(l).
\]
For every \(\theta>24\), this system has exactly nine real solution pairs \((h,l)\). Hence this one invariant branch yields nine distinct splitting Gibbs measures in the source construction.

## Assumptions and scope
The order \(k\) is an integer with \(k\ge4\), the Potts coupling is ferromagnetic, and \(\theta>24\). The statement concerns only the fixed matrix \(M\) above and only the invariant set \(I_1\). It is an exact count of solutions on that branch, not a count of all Gibbs measures of the Potts model. The constant \(24\) is a uniform sufficient bound produced by the proof; no sharpness claim is made for it.

## Proof
Set \(t=e^{h/k}>0\). The first equation is equivalent to
\[
F_{k,\theta}(t)=t^{k+1}-\theta t^k+(\theta+1)t-2=0.
\]
The coefficient signs of \(F_{k,\theta}\) have three variations, so Descartes' rule gives at most three positive roots. We now exhibit three. First, \(F_{k,\theta}(0)=-2\), while for \(r=2/\theta\),
\[
F_{k,\theta}(r)>\frac{2}{\theta}-\frac{2^k}{\theta^{k-1}}>0
\]
when \(k\ge4\) and \(\theta>24\). Also \(F_{k,\theta}(1)=0\). Finally,
\[
F_{k,\theta}(\theta/2)
=-\frac{\theta^{k+1}}{2^{k+1}}+\frac{\theta(\theta+1)}2-2<0,
\]
whereas \(F_{k,\theta}(\theta)=\theta(\theta+1)-2>0\). Thus there are exactly three positive roots
\[
0<t_-<1=t_0<t_+<\theta.
\]
The last inequality also follows directly from the fixed-point form
\[
t=\frac{\theta t^k+2}{\theta+t^k+1}.
\]

Fix one of these roots \(t\), put \(x=e^{l/(k-1)}>0\), and set \(\alpha=t^{1/(k-1)}\). Since \(f_\theta(h)=\log t\), the second equation is equivalent to
\[
x^k-\alpha\theta x^{k-1}+(\theta+1)x-2\alpha=0.
\]
Writing \(x=\alpha y\) gives the simpler polynomial
\[
H_t(y)=t y^k-\theta t y^{k-1}+(\theta+1)y-2.
\]
Again there are exactly three coefficient-sign variations, so \(H_t\) has at most three positive roots. We show that it has three in each of the three cases.

For \(t=t_-<1\),
\[
H_t(0)<0,\qquad H_t(1)=(\theta-1)(1-t)>0.
\]
Because the fixed-point formula and \(t<1\) give \(t>2/(\theta+2)\),
\[
H_t(\theta/2)
=-\frac{t\theta^k}{2^k}+\frac{\theta(\theta+1)}2-2<0
\]
for \(k\ge4\), \(\theta>24\); here it is enough to note that
\[
\frac{\theta^4}{8(\theta+2)}>\frac{\theta(\theta+1)}2.
\]
Since \(H_t(y)\to+\infty\), there is one positive root in each of \((0,1)\), \((1,\theta/2)\), and \((\theta/2,\infty)\).

For \(t=t_0=1\), one has
\[
H_1(0)<0,\qquad
H_1(1/2)=\theta\left(\frac12-\frac1{2^{k-1}}\right)-\frac32+\frac1{2^k}>0,
\]
\[
H_1(2)=2^k-\theta(2^{k-1}-2)<0,
\]
and again \(H_1(y)\to+\infty\). Hence there are three positive roots.

For \(t=t_+>1\), take \(y=3/\theta\). Since \(t<\theta\), \(k\ge4\), and \(\theta>24\),
\[
H_t(3/\theta)
>1+\frac3\theta-9\left(\frac3\theta\right)^{k-3}
\ge 1-\frac{24}{\theta}>0.
\]
On the other hand, \(H_t(0)<0\) and \(H_t(1)=(\theta-1)(1-t)<0\), while \(H_t(y)\to+\infty\). Thus there is one positive root in each of \((0,3/\theta)\), \((3/\theta,1)\), and \((1,\infty)\).

Descartes' rule makes each of these lower bounds exact. Therefore each of the three admissible \(t\)-values gives exactly three admissible \(l\)-values, for exactly \(3\times3=9\) pairs \((h,l)\). The source's boundary-law correspondence assigns a splitting Gibbs measure to every such solution, and the nine pairs are distinct.

## Verification
The algebraic substitutions above are bijective because exponentiation maps real fields to positive variables. `verify.py` independently reconstructs the three \(t\)-roots and the three associated \(y\)-roots for representative orders and parameters, substitutes the reconstructed \((h,l)\) pairs into the original two equations, and checks the sign inequalities used in the proof. These finite computations are corroborative only; the proof is the all-order sign-and-Descartes argument above.

## Relationship to prior work
Rahmatullaev and Dekhkonov introduce the matrix-valued two-boundary construction, derive the invariant-set system \(I_1\), and prove a general theorem giving at least seven Gibbs measures under a derivative condition. In their Remark 1 they explicitly note that, when \(b=0\), the \(I_1\) system can have more than three solutions, but they do not count them. Their comparison section also records the familiar three translation-invariant solutions above the Potts critical point. The result here specializes to the natural coupled matrix \(M=((k,0),(1,k-1))\) and turns that qualitative possibility into an exact nine-solution theorem on a uniform low-temperature region.

Targeted searches by the source identifier, the matrix parameters, the nine-solution formulation, and equivalent fixed-point language did not locate a published statement implying this exact branch count. Earlier translation-invariant or periodic classifications concern different symmetry classes and do not dominate this two-value construction.

## Limitations
The bound \(\theta>24\) is sufficient and is not claimed sharp. The theorem counts only solutions on \(I_1\) for the specified matrix. It does not classify the other invariant sets, all splitting Gibbs measures, extremality, reconstruction, stability, or thermodynamic dominance. A weakly indexed equivalent calculation under different variables remains a literature risk.

## References
1. M. M. Rahmatullaev and Zh. D. Dekhkonov, “Potts model on a Cayley tree: a new class of Gibbs measures,” arXiv:2211.12128v1 (first public version 2022-11-22); Theoretical and Mathematical Physics 215 (2023), DOI:10.1134/S0040577923040086; original DOI:10.4213/tmf10374.
2. C. Külske, U. A. Rozikov, and R. M. Khakimov, “Description of translation-invariant splitting Gibbs measures for the Potts model on a Cayley tree,” Journal of Statistical Physics 156 (2014), 189–200, cited by the primary source for the scalar translation-invariant equation.
