# Exact \(C\)-approximate Birkhoff symmetry for the dual cubic planes
## Finding
Let \(\chi_C(E)\) denote the optimal global Chmieliński \(C\)-approximate-symmetry parameter of Birkhoff--James orthogonality in a real Banach space \(E\). Then
\[
\boxed{\chi_C(\ell_3^2)=\chi_C(\ell_{3/2}^2)=\left(\frac{78\sqrt3-135}{16}\right)^{1/6}}\approx0.42916063195784049.
\tag{1}
\]
The maximizing ordered Birkhoff--James pairs in the cubic plane are unique up to signed coordinate permutations and changing the sign of the orthogonal partner. Explicit representatives are
\[
t_0=\left(\frac{1-\sqrt{2\sqrt3-3}}{1+\sqrt{2\sqrt3-3}}\right)^{1/3},
\quad x=\frac{(1,t_0)}{(1+t_0^3)^{1/3}},
\quad y=\frac{(-t_0^2,1)}{(1+t_0^6)^{1/3}}.
\tag{2}
\]
The corresponding sharp pairs in the dual plane follow from a duality principle proved below.

## Assumptions and scope
Every space considered is real. For nonzero \(x\in E\), write
\[
J_E(x)=\{f\in S_{E^*}:f(x)=\|x\|\}.
\]
Birkhoff--James orthogonality and its Chmieliński approximation are defined by
\[
x\perp_B y\ \Longleftrightarrow\ \|x+\lambda y\|\ge\|x\|\ \text{for all }\lambda\in\mathbb R,
\]
\[
x\perp_B^\varepsilon y\ \Longleftrightarrow\ \exists f\in J_E(x): |f(y)|\le\varepsilon\|y\|,
\quad 0\le\varepsilon<1.
\tag{3}
\]
The second equivalence is the standard functional characterization of Chmieliński approximate Birkhoff--James orthogonality. Let
\[
\chi_C(E)=\inf\{\varepsilon\in[0,1): \forall x,y\ne0,\ x\perp_B y\Rightarrow y\perp_B^\varepsilon x\}.
\tag{4}
\]
For smooth spaces the norming functional is unique. In every finite-dimensional smooth strictly convex space, the set of unit Birkhoff--James pairs is compact, the duality map is continuous, and no such pair can have reverse residual \(1\): otherwise strict convexity would give \(x=\pm y\), contradicting Birkhoff--James orthogonality. Thus its maximum is strictly less than \(1\). In such spaces,
\[
\chi_C(E)=\sup_{\substack{x,y\in S_E\\x\perp_B y}}|J_E(y)(x)|.
\tag{5}
\]

## Proof
**Duality lemma.** If \(E\) is finite-dimensional, real, smooth and strictly convex, then
\[
\chi_C(E)=\chi_C(E^*).
\tag{6}
\]
Indeed, the normalized duality map \(j_E:S_E\to S_{E^*}\) is bijective: smoothness supplies uniqueness of the norming functional, finite-dimensional norm attainment supplies existence of a norming vector for each \(f\in S_{E^*}\), and strict convexity makes that vector unique. Also
\[
j_{E^*}(j_E(x))=x
\]
under the canonical embedding in \(E^{**}\). Every ordered unit pair \((x,y)\) with \(x\perp_B y\) gives an ordered dual pair
\[
(a,b)=(j_E(y),j_E(x)).
\]
It satisfies \(a\perp_B b\), because
\[
j_{E^*}(a)(b)=y(j_E(x))=0.
\]
The reverse residual of the dual pair is
\[
|j_{E^*}(b)(a)|=|x(j_E(y))|=|j_E(y)(x)|.
\]
This operation is bijective on the ordered Birkhoff-pair sets, by the duality-map inverse. Taking suprema proves (6), and it transports all maximizing configurations.

**Cubic-plane calculation.** Now take \(E=\ell_3^2\), which is smooth and strictly convex. For each unit vector \(z=(z_1,z_2)\),
\[
j_E(z)=(z_1|z_1|,z_2|z_2|).
\tag{7}
\]
By signed coordinate permutation symmetry, a non-axis base unit vector has the form
\[
x=\frac{(1,t)}{(1+t^3)^{1/3}},\quad t>0.
\]
Its unit Birkhoff--James orthogonal partners are exactly
\[
y=\pm\frac{(-t^2,1)}{(1+t^6)^{1/3}},
\tag{8}
\]
because the kernel of the unique norming functional \(j_E(x)\) is one-dimensional. The limiting axis cases yield reverse residual zero.

From (7)--(8), direct computation gives
\[
D(t)=|j_E(y)(x)|=
\frac{|t-t^4|}{(1+t^3)^{1/3}(1+t^6)^{2/3}}.
\tag{9}
\]
Put \(u=t^3\). Then
\[
D(t)^3=\frac{u|1-u|^3}{(1+u)(1+u^2)^2}.
\tag{10}
\]
Expression (10) is invariant under \(u\mapsto1/u\), corresponding to coordinate interchange, so it suffices to maximize over \(0\le u\le1\). Set
\[
k=\frac{1-u}{1+u},\qquad 0\le k\le1.
\]
One obtains the rational profile
\[
D^3=H(k)=\frac{k^3(1-k^2)}{(1+k^2)^2}.
\tag{11}
\]
Its derivative factors exactly as
\[
H'(k)=\frac{k^2(3-6k^2-k^4)}{(1+k^2)^3}.
\tag{12}
\]
The numerator factor \(3-6w-w^2\) has a unique positive root
\[
w_0=2\sqrt3-3\in(0,1).
\]
Thus \(H\) strictly increases on \((0,\sqrt{w_0})\) and strictly decreases on \((\sqrt{w_0},1)\); endpoints give zero. Its unique maximum occurs at
\[
k_0=\sqrt{2\sqrt3-3}.
\]
Exact simplification gives
\[
H(k_0)^2=\frac{78\sqrt3-135}{16}.
\tag{13}
\]
Because \(D^6=H^2\), (13) yields the sharp value in (1). Since (12) has only one interior maximum, all maximizing ordered pairs in \(\ell_3^2\) are precisely the symmetries of (2). Finally, (6) gives the exact same sharp constant for \(\ell_{3/2}^2\) and transports its maximizing ordered pairs as claimed.

## Verification
The bundled `verify.py` checks the derivative identity (12) and the radical identity (13) exactly in symbolic arithmetic, the cubic support-functional and Birkhoff identities on representative points, and the duality-map reverse-residual correspondence. It also reports independent numerical scans of (9) and (11) as supplementary sanity checks.

The continuum maximum does not depend on finite sampling: it follows from the exact rational expression and derivative-sign analysis in (11)--(13). The finite-dimensional duality lemma is proved geometrically, not inferred from examples.

## Relationship to prior work
Chmieliński, Khurana and Sain's 2020 preprint (subsequently published in *Results in Mathematics*) develops global and local approximate symmetry in both the Chmieliński and Dragomir senses. Its smooth-space and finite-dimensional conclusions are qualitative; the inspected full text supplies the framework in (3) but not the exact cubic-plane threshold (1) or the duality statement (6).

Bose, Roy and Sain's 2022 paper gives a support-functional description of ordinary Birkhoff--James orthogonality in \(\ell_p\) and studies local symmetry points. These statements do not compute the sharp global \(C\)-approximate reversal defect. An indexed exact result for the same Hölder-dual pair computes the **Dragomir** approximate-symmetry parameter, not the Chmieliński \(C\)-parameter in (3): their definitions and sharp values differ.

Chmieliński and Wójcik's 2018 article introduces a geometric constant associated with global approximate symmetry; only its abstract and bibliographic metadata could be inspected. This is a genuine residual novelty risk and no claim is made that its full text lacks an equivalent result.

## Limitations
The explicit radical and maximizing orbit are established for the two real cubic Hölder-dual planes, not for all \(\ell_p^2\) planes. The duality lemma applies to finite-dimensional real spaces that are both smooth and strictly convex; neither hypothesis is dropped here.

The 2018 source was not inspected in full, and semantic-index searches cannot certify absolute novelty. No independent validation or audit has been conducted.

## References
1. J. Chmieliński, D. Khurana and D. Sain, “Local approximate symmetry of Birkhoff-James orthogonality in normed linear spaces,” arXiv:2012.08162v1, first public 15 December 2020; *Results in Mathematics* 76 (2021), article 136, doi:10.1007/s00025-021-01437-y. Primary MSC 46B20.
2. S. Bose, S. Roy and D. Sain, “Birkhoff-James Orthogonality and its local symmetry in some sequence spaces,” arXiv:2205.11586v1, first public 23 May 2022.
3. J. Chmieliński and P. Wójcik, “Approximate symmetry of Birkhoff orthogonality,” *Journal of Mathematical Analysis and Applications* 461 (2018), 625–640, doi:10.1016/j.jmaa.2018.01.031.
4. J. Chmieliński, T. Stypuła and P. Wójcik, “Approximate orthogonality in normed spaces and its applications,” *Linear Algebra and its Applications* 531 (2017), 305–317, doi:10.1016/j.laa.2017.06.001.
