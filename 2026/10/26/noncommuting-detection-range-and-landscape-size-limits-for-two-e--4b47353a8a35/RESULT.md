# Noncommuting detection-range and landscape-size limits for two ecological traps

## Finding
Consider a habitat transect with \(n\ge3\) equally spaced sites, indexed \(0,\ldots,n-1\), and two distinct traps at sites \(a<b\). An animal at site \(i\) is detected independently by the two traps with respective probabilities \(q^{|i-a|}\) and \(q^{|i-b|}\), where \(0<q<1\). The animal's site is uniform on the transect. Write \(P_n(a,b;q)\) for its probability of being detected by at least one trap and \(F_n=nP_n\).

**Theorem.** (i) For any prescribed integer separation \(s=b-a\), the maximizing locations have exactly the balanced boundary gaps \(a=\lfloor(n-1-s)/2\rfloor\) and \(r=n-1-b=\lceil(n-1-s)/2\rceil\), or their mirror image. Thus an exact global optimizer is obtained by evaluating only \(n-1\) centered separations.

(ii) Fix \(q\in(0,1)\). For *every* sequence of global optimizers as \(n\to\infty\),
\[
\frac{a_n}{n-1}\longrightarrow\frac13,
\qquad\frac{b_n}{n-1}\longrightarrow\frac23.
\]
More precisely, the boundary gap \(a_n\), intertrap gap \(b_n-a_n\), and right boundary gap \(n-1-b_n\) all equal \(n/3+O_q(\log n)\).

(iii) Conversely, if the detection range is sent to infinity *before* the landscape length, then the optimal locations approach quarters: for any sequence of placements selected as limits of global optimizers for \(q\uparrow1\) at each fixed \(n\),
\[
\frac{a_n}{n-1}\longrightarrow\frac14,
\qquad\frac{b_n}{n-1}\longrightarrow\frac34.
\]
Accordingly, the two iterated limits of the normalized optimal-placement pair do not commute.

(iv) The first transect length at which the optimal pair depends on \(q\) is \(n=7\). For \(n=3,4,5,6\), the optimizers are, respectively, \((0,2)\); \((0,2),(1,3)\); \((1,3)\); and \((1,4)\), for all \(q\in(0,1)\). For \(n=7\), let \(q_*\in(0,1)\) be the unique root of \(q_*^3+2q_*-1=0\), numerically \(0.45339765151641054\ldots\). The complete set of optimizers is \(\{(1,4),(2,5)\}\) when \(q<q_*\), \(\{(1,5)\}\) when \(q>q_*\), and their union at equality.

## Assumptions and scope
There are exactly two distinct fixed traps and a *single* potential animal site, uniform among \(n\) sites. Distances are integer graph distances along a path. Trap detections are conditionally independent given the animal's site. At a trap's own site detection is certain; this is a simplifying idealization, not a general capture-recapture model. The optimization criterion is the expected detection probability for an animal whose location is unknown, equivalently average site coverage; it is **not** precision of estimated density, expected time to capture, or a guarantee for the worst-covered site. For every \(n\) and \(q\), maximizers exist because there are finitely many pairs.

## Proof
For notational convenience, set \(s=b-a\) and \(r=n-1-b\); thus \(a+s+r=n-1\). Conditional independence gives the exact objective
\[
F_n(a,b;q)=\sum_{i=0}^{n-1}\bigl(q^{|i-a|}+q^{|i-b|}-q^{|i-a|+|i-b|}\bigr).
\]
Summing the two geometric single-trap terms and splitting the overlap term into the left exterior, the intertrap interval, and the right exterior yields
\[
\begin{aligned}
D_n(a,b;q)&:=\frac{2(1+q)}{1-q}-F_n(a,b;q)\\
&=\frac{q(1+q^s)}{1-q}(q^a+q^r)
+q^s\left(s+1+\frac{q^2(2-q^{2a}-q^{2r})}{1-q^2}\right).
\end{aligned}
\tag{1}
\]
The identity is exact for all permissible parameters, including \(a=0\) and \(r=0\).

**Fixed-separation centering.** For fixed \(s\) and \(a+r=n-1-s\), the only varying part of \(D_n\) is \(H_s(a)+H_s(r)\), where
\[
H_s(x)=\alpha_s q^x-\beta_s q^{2x},\quad
\alpha_s=\frac{q(1+q^s)}{1-q},\quad
\beta_s=\frac{q^{s+2}}{1-q^2}.
\]
For \(x\ge0\),
\[
H_s''(x)=(\log q)^2q^x\bigl(\alpha_s-4\beta_s q^x\bigr)>0.
\]
Indeed, \(\alpha_s/(4\beta_s)=(1+q^s)(1+q)/(4q^{s+1})>1\); the final inequality follows from \(s\ge1\), \(q<1\), and \((1+q)^2>4q^2\). Strict convexity makes \(H_s(a)+H_s(r)\) smallest at the two nearest integers to \((n-1-s)/2\), and nowhere else. This proves (i).

**Fixed-range, large-landscape limit.** Let \(m=\min\{a+1,r+1,s\}\). Every displayed summand in (1) is nonnegative. In particular,
\[
D_n(a,b;q)\ge q^m.
\tag{2}
\]
Choose a comparison placement whose three gaps \(a,r,s\) differ by at most one, possible since their sum is \(n-1\). Formula (1) gives, for some constant \(C_q<\infty\) independent of \(n\),
\[
0<D_n(\text{comparison};q)\le C_q(n+1)q^{\lfloor(n-1)/3\rfloor}.
\tag{3}
\]
A global maximizer of \(F_n\) minimizes \(D_n\), so (2)–(3), after taking logarithms and noting \(\log q<0\), imply \(m\ge n/3-O_q(\log n)\). Since \((a+1)+(r+1)+s=n+1\), each of these three nonnegative gaps is \(n/3+O_q(\log n)\). Therefore \(a/n\to1/3\) and \(b/n\to2/3\). The choice of maximizer was arbitrary, proving (ii).

**Long-range first, then large-landscape limit.** For each fixed \(n\), put \(\varepsilon=1-q\). The exact missed-detection probability at site \(i\) is \((1-q^{|i-a|})(1-q^{|i-b|})\), hence uniformly over the finitely many placements,
\[
n-F_n(a,b;q)=\varepsilon^2 G_n(a,b)+O_n(\varepsilon^3),\quad
G_n(a,b)=\sum_{i=0}^{n-1}|i-a||i-b|.
\tag{4}
\]
Any location pair occurring as a limit of maximizers as \(q\uparrow1\) must therefore minimize \(G_n\). Write \(u=a/(n-1)\), \(v=b/(n-1)\). Uniform Riemann-sum convergence over all these pairs gives
\[
\frac{G_n(a,b)}{(n-1)^3}
=I(u,v)+O(n^{-1}),\qquad
I(u,v)=\int_0^1 |x-u||x-v|\,dx.
\tag{5}
\]
For \(0\le u\le v\le1\), set \(c=(u+v)/2\) and \(d=(v-u)/2\). Direct integration yields
\[
I(u,v)=c^2-c+\frac13+\frac83d^3-d^2.
\tag{6}
\]
Subject to \(0\le d\le\min\{c,1-c\}\), this function has the unique global minimum at \(c=1/2,d=1/4\): for every fixed \(d\) the unconstrained minimizing midpoint \(c=1/2\) is admissible, and the resulting derivative in \(d\) is \(2d(4d-1)\). Thus the unique continuum minimizing sites are \(u=1/4,v=3/4\). Uniformity of (5), compactness, and uniqueness force *every* sequence of minimizing discrete pairs to converge to these fractions. This proves (iii).

**First finite change.** By (i), only centered separations need checking. For \(n=3,4,5,6\), exact subtraction of the corresponding objective polynomials shows the winners in (iv) strictly dominate all other separations for \(0<q<1\). The coefficient identities (all pairs) are reproduced by `verify.py`; their factors are products of \(q\), \((1-q)^2\), and positive factors such as \(q^2-q+1\), \(2-q^3\), and \(1+2q-q^2\). For \(n=7\), the centered separation-three arrangement \((1,4)\) dominates all centered separations except four for every \(0<q<1\). A direct polynomial identity gives
\[
F_7(1,5;q)-F_7(1,4;q)
=q^2(1-q)^2(q^3+2q-1).
\tag{7}
\]
The function \(q^3+2q-1\) increases strictly and changes sign once in \((0,1)\), establishing the complete classification. Reflection produces the companion separation-three pair \((2,5)\). Exact factor certificates for domination of the other separations are checked by the standalone program, and their signs follow directly from \(0<q<1\), not from numerical sampling. This proves (iv).

## Verification
Run `python verify.py > verification_certificate.json` in the extracted package directory. The checker uses the Python standard library and exact rational arithmetic. It independently enumerates the original finite sum and the closed form (1) for 51,980 placements, checks centering for 5,980 fixed-separation cases, and compares full and centered searches for 460 settings. It also compares 15 exact polynomial identities (including the seven-site transition) and checks the seven-site phase diagram at 20 rational detection parameters. The supplied certificate is the exact output. Equations (2)–(6) are general analytical arguments; finite experiments alone would not establish them.

## Relationship to prior work
Dhillon, Chakrabarty and Iyengar (2002) explicitly use exponentially distance-decaying independent sensor detection on a grid and optimize the *number* of sensors subject to a sitewise probability threshold by a heuristic. Their model is closely related, but their stated objective and analysis do not imply the two-fixed-trap **average** detection optimum, the strict centering reduction, or the noncommuting limits. Sun, Fuller and Royle (2014) investigate spatial capture–recapture trap configurations and parameter-estimation performance through simulations using a half-normal distance kernel; they do not prove these exact two-trap geometric-kernel statements. Frasca and coauthors (arXiv:1404.7711) study sensors with independent outright failures, minimizing expected *maximum nearest-active-sensor distance*; their objective and failure model differ from distance-decaying independent detections. Borchers and Efford (2007) provide foundational spatial capture-recapture likelihood modeling rather than the claimed optimization classification. These distinctions are comparisons of mathematical claims and their assumptions, not evidence of global bibliographic uniqueness.

## Limitations
The result is a structural design theorem in a stylized one-dimensional landscape. It does not claim statistical efficiency for abundance estimation, handle habitat-dependent animal density, trap interference, false positives, repeated trapping, imperfect detection at zero distance, cost asymmetry, or non-geometric kernels. The order-of-limits discrepancy concerns mathematically distinct scaling regimes; at a fixed large but finite \(n\), a very long detection range can make quarter placement preferable. The seven-site cutoff is for the exact stated discrete kernel, not a universal empirical threshold. Prior-work uncertainty remains for alternative formulations in facility location and sensor-coverage research. Independent scientific audit has not been performed.

## References
1. S. S. Dhillon, K. Chakrabarty, S. S. Iyengar, *Sensor Placement for Grid Coverage under Imprecise Detections*, Proceedings of FUSION 2002, pp. 1581–1587, DOI:10.1109/ICIF.2002.1021005. Full article material inspected via the author-uploaded public text.
2. C. C. Sun, A. K. Fuller, J. A. Royle, *Trap Configuration and Spacing Influences Parameter Estimates in Spatial Capture-Recapture Models*, PLOS ONE 9 (2014), e88025, DOI:10.1371/journal.pone.0088025. First published online 2014-02-05; primary full text inspected.
3. P. Frasca, F. Garin, B. Gerencsér, J. M. Hendrickx, *Optimal One-Dimensional Coverage by Unreliable Sensors*, arXiv:1404.7711 (first submitted 2014-04-30). Primary preprint inspected.
4. D. L. Borchers, M. G. Efford, *Spatially Explicit Maximum Likelihood Methods for Capture–Recapture Studies*, Biometrics 64 (2008), 377–385, DOI:10.1111/j.1541-0420.2007.00927.x (online 2007-10-26). Used as background for the distinction between site detection and density inference.
