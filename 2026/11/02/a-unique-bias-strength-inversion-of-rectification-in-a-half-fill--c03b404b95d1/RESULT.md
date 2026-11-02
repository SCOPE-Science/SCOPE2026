# A unique bias-strength inversion of rectification in a half-filled disordered exclusion ring

## Finding

For the site-disordered, two-particle asymmetric simple exclusion process on four cyclic vertices, the stationary current rectification can **reverse sign as the magnitude of the driving bias increases**, even though all rates and the particle number remain fixed. Its exact zero-set and polarity phase diagram are determined by two cubic invariants of four site rates. At nonzero nonmaximal bias, globally odd current occurs exactly for reflection-symmetric site-rate arrangements; outside this set, at most one finite-bias rectification reversal occurs. The fully distinct landscape \((1,2,4,9)\) has a unique inversion at \(|\varepsilon|=\sqrt{7/99}\). This is distinct from the fixed-polarity response in the single-hole sector of the same ring.

## Assumptions and scope

Sites are labelled \(0,1,2,3\) modulo four. Exactly two sites are occupied at all times. A particle at occupied site \(i\) attempts a clockwise step to vacant \(i+1\) with rate \(p w_i\), and an anticlockwise step to vacant \(i-1\) with rate \(q w_i\), where \((w_0,w_1,w_2,w_3)=(a,b,c,d)\), each positive, and

\[
p=(1+\varepsilon)/2,\qquad q=(1-\varepsilon)/2,\qquad -1<\varepsilon<1.
\]

A failed move into an occupied site has no effect. The chain on its six two-occupied-site configurations is irreducible and has a unique stationary law. Let \(J(\varepsilon)\) be the stationary signed clockwise minus anticlockwise hop rate **per bond** (the total signed hop rate divided by four). We study \(\mathcal R(\varepsilon)=J(\varepsilon)+J(-\varepsilon)\). For all statements about its sign we require \(0<|\varepsilon|<1\), excluding unbiased driving and the totally asymmetric endpoints, where \(\mathcal R=0\) automatically.

Define

\[
A=a+c,\quad B=b+d,\quad U=ac,\quad V=bd,
\]
\[
\alpha=UB-VA,\qquad \beta=(A+B)(U-V)+AB(B-A),
\]
\[
H(p,q)=\alpha(p^2+q^2)+\beta pq.
\]

**The exact phase classification** is:

1. For \(0<|\varepsilon|<1\), \(\operatorname{sgn}\mathcal R(\varepsilon)=-\operatorname{sgn}[(a-c)(b-d)H(p,q)]\).
2. The current is odd for every bias \(\varepsilon\in(-1,1)\) if and only if \(a=c\), \(b=d\), or the unordered pairs \(\{a,c\}\) and \(\{b,d\}\) agree. These are precisely the reflection-symmetric patterns of the four-cycle.
3. Without one of these reflections, there is at most one **positive bias magnitude** \(|\varepsilon|\in(0,1)\) at which \(\mathcal R=0\) (its two signed realizations are \(\varepsilon\) and \(-\varepsilon\)). An interior zero with a strict polarity switch occurs if and only if \(\alpha(2\alpha+\beta)<0\), at

\[
\varepsilon_*^2=\frac{2\alpha+\beta}{\beta-2\alpha} \in(0,1).
\]

If the endpoint product is zero but the pattern has no reflection, no **interior** switch occurs. If \((a,b,c,d)=(1,2,4,9)\), then \(\alpha=-46\), \(\beta=106\), and

\[
H(p,q)=\frac{7-99\varepsilon^2}{2},\qquad
|\varepsilon_*|=\sqrt{\frac7{99}}.
\]

Here \((a-c)(b-d)>0\); therefore \(\mathcal R<0\) for \(0<|\varepsilon|<\sqrt{7/99}\) and \(\mathcal R>0\) for \(\sqrt{7/99}<|\varepsilon|<1\).

## Proof

Write the six configurations in lexicographic order as \(01,02,03,12,13,23\), denoting their occupied sites. Construct their generator \(Q\): for every configuration \(C\), every occupied \(i\in C\), and each allowed destination \(i\pm1\notin C\), add the rate \(pw_i\) or \(qw_i\) to \(Q_{C,C'}\), where \(C'=(C\setminus\{i\})\cup\{i\pm1\}\). Complete the diagonal by making every row sum zero. This fully specifies a six-by-six matrix with polynomial entries. Put \(\tau_C=\det((-Q)_{C^c,C^c})\) and \(D=\sum_C\tau_C\). By the finite-state Markov-chain tree theorem, all \(\tau_C>0\), \(D>0\), and \(\pi_C=\tau_C/D\) is the exact stationary law. Positivity also holds at nonnegative endpoints by irreducibility of this ring process.

Let \(v_C\) be the signed total instantaneous jump intensity from configuration \(C\), computed by summing the clockwise rates minus anticlockwise rates of all its permitted moves. Then \(4J=\sum_C\pi_Cv_C\). Direct expansion of these six finite cofactors, followed by collecting monomials, gives the **exact polynomial identity**

\[
N:=\sum_C \tau_Cv_C
=4abcd(p-q)(p+q)(p^2+q^2)(Ap+Bq)(Aq+Bp).
\]

Hence \(4J=N/D\). The accompanying standalone symbolic checker constructs the generator directly, computes all six cofactors, and proves this identity by polynomial subtraction with zero remainder; it does not infer an identity from numerical samples.

Now let \(D'=D(q,p)\) and \(N'=N(q,p)\), with site rates unchanged. A second exact cofactor expansion yields

\[
ND'+N'D=-4abcd\,pq(a-c)(b-d)(p-q)^2(p+q)(p^2+q^2)\,
(Ap+Bq)(Aq+Bp)H(p,q).
\]

Since \(4\mathcal R=(ND'+N'D)/(DD')\), all factors other than the explicit minus sign, \((a-c)(b-d)\), and \(H\) are strictly positive for \(0<|\varepsilon|<1\). This proves the first assertion.

To classify globally odd current, it is enough to consider the case \(a\ne c\), \(b\ne d\). Then the second identity says that \(\mathcal R\) vanishes at every interior bias precisely when \(H\) is the zero polynomial. Because \(p^2+q^2\) and \(pq\) are linearly independent homogeneous quadratics, this is equivalent to \(\alpha=\beta=0\). The equation \(\alpha=0\) gives \(U=VA/B\), and substitution into the second equation gives

\[
(A-B)\left[\frac{V(A+B)}{B}-AB\right]=0.
\]

If \(A\ne B\), this forces \(V=AB^2/(A+B)\) and \(U=A^2B/(A+B)\). But the elementary positive-pair arithmetic-geometric-mean bounds \(U\le A^2/4\) and \(V\le B^2/4\) would imply simultaneously \(A\ge3B\) and \(B\ge3A\), impossible. Therefore \(A=B\), then \(U=V\), and the two opposite-site pairs have identical sum and product: \(\{a,c\}=\{b,d\}\). Conversely, every listed reflection condition nullifies the rectification identity. This proves the iff classification, including the nonsymmetric cases \(a=c\) and \(b=d\) individually.

Finally, using the bias parametrization,

\[
H=\tfrac14\big[(2\alpha+\beta)+(2\alpha-\beta)\varepsilon^2\big].
\]

This is affine in \(\varepsilon^2\in(0,1)\). Its endpoint signs are the signs of \(2\alpha+\beta\) and \(\alpha\), respectively; thus a single strict interior crossing exists exactly for \(\alpha(2\alpha+\beta)<0\), at the displayed expression. No additional crossings are possible. Substituting the four stated integer rates gives \(\alpha=-46\), \(\beta=106\), proving the exact witness and signs. All quantifiers and exceptional cases follow.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy. It reconstructs the six-state generator using occupied-to-vacant moves, calculates all six stationary cofactors, and checks **two exact multivariate polynomial identities** by expansion to zero. It further verifies the analytical witness and performs 32 separately solved six-state stationary systems at rational parameters without using the tree formula in the stationary solver. Finally it checks the symmetry-elimination identity used with AM-GM. The executed program returned a PASS. Unlike finite sampling, the exact symbolic zero-remainder identities cover every admissible parameter value.

## Relationship to prior work

Sakai and Akimoto (2025/2026, arXiv:2512.03316) established the stochastic site-trap model and its general bias-symmetry mechanisms; their complete manuscript, including its model, nonlinear regime, conclusions and appendices C–F, treats general criteria and simulations, not the exact six-configuration formula, reflection-only equivalence at half filling or the unique finite-strength inversion proved here. Goldstein and Speer's 1998 theorem concerns direction invariance in the totally asymmetric limit, which corresponds to the zero rectification endpoint \(|\varepsilon|=1\) and does not imply an interior crossover. Juhász, Santen and Iglói (2006) analyze large-disordered-system transport scaling, not this exact finite-ring classification. A related earlier one-hole, four-site calculation has a field-independent rectification sign; that result does not imply the half-filled strength-driven sign change.

## Limitations

The claim concerns exactly two indistinguishable particles on four sites with strictly positive departure rates and a spatially uniform field multiplier. It is not a claim about the thermodynamic limit, random disorder averages, open boundary models, time-dependent transients or arbitrary bond-disorder rates. A stronger unlocated exact finite-particle ring-current theorem could subsume the result; the closest older full manuscripts not directly obtained remain a priority risk. The analytical result has received only self-review; no independent audit has been performed.

## References

- I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, first public 2025-12-03, arXiv:2512.03316, https://arxiv.org/abs/2512.03316 (primary manuscript v2, especially model, Sec. III, Sec. IV, appendices C–F).
- S. Goldstein and E. R. Speer, *Reflection invariance of the current in the totally asymmetric simple exclusion process with disorder*, Physical Review E 58, 4226 (1998), https://doi.org/10.1103/PhysRevE.58.4226.
- R. Juhász, L. Santen and F. Iglói, *Partially Asymmetric Exclusion Processes with Sitewise Disorder*, Physical Review E 74, 061101 (2006), https://arxiv.org/abs/cond-mat/0607366.
