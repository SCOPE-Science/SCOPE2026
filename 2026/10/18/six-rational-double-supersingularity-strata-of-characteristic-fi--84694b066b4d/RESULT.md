# Six rational double-supersingularity strata of characteristic-five Ciani quartics

## Finding
Let \(k=\overline{\mathbb F}_5\) and
\[
C_{r,s,t}:\quad X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2=0.
\]
On the smooth parameter locus defined below, set
\[
\begin{aligned}
H_1&=2(rt-2s)^2+(r^2-4)(t^2-4),\\
H_2&=2(rs-2t)^2+(r^2-4)(s^2-4),\\
H_3&=2(st-2r)^2+(s^2-4)(t^2-4).
\end{aligned}
\]
The Jacobian has \(a\)-number \(\#\{i:H_i=0\}\) and \(5\)-rank \(3-\#\{i:H_i=0\}\). In particular, the locus of \(a\)-number at least two is a union of exactly six rational irreducible curves. Put
\[
f(u)=\frac{2-2u^2}{2u^2-1},\qquad
U=\{u\in k:u\ne0,\ u^2\ne4,\ 2u^2\ne1\}.
\]
Two components are the images of
\[
u\longmapsto (f(u),u,u),\qquad
u\longmapsto(-f(u),u,-u)
\]
for \(u\in U\); the remaining four are their cyclic coordinate permutations. Every component is isomorphic to \(U\). There are precisely eight triple-intersection points (each incident with three components, each component incident with four such points), and no other component intersections. They are exactly the superspecial parameters:
\[
r^2=s^2=t^2=q,\quad rst=q^2+2,\quad q^2+2q-1=0.
\]
There are two choices of \(q\), each giving four parameter triples. The other points on the six components have \(a=2\), \(5\)-rank one, and the triple points have \(a=3\), \(5\)-rank zero.

## Assumptions and scope
All parameters are in \(k=\overline{\mathbb F}_5\). The Ciani plane quartic is smooth precisely when
\[
(r^2-4)(s^2-4)(t^2-4)(r^2+s^2+t^2-rst-4)\ne0.
\]
This is the labelled affine coefficient space, **not** a claim of eight distinct geometric isomorphism classes or a description of an unmarked moduli quotient. All integers and polynomial expressions are interpreted in characteristic five. Every curve under these assumptions is smooth of genus three.

## Proof
**Elliptic quotients and rank.** The three commuting coordinate-sign involutions yield genus-one quotient curves \(E_1,E_2,E_3\). The known degree-eight isogeny \(\operatorname{Jac}(C)\to E_1\times E_2\times E_3\) has degree prime to five; thus it induces an isomorphism of their \(5\)-torsion group schemes and preserves both \(a\)-number and \(5\)-rank. Completing the square for the first elliptic quotient gives
\[
v^2=(r^2-4)u^4+2(rt-2s)u^2+(t^2-4).
\]
For a nonsingular elliptic quartic \(v^2=Au^4+Bu^2+C\) in characteristic five, the Hasse invariant is proportional to the coefficient of \(u^4\) in \((Au^4+Bu^2+C)^2\), namely \(B^2+2AC\). Substituting the first quotient gives \(2H_1\); cyclically it gives \(2H_2\) and \(2H_3\). Every elliptic quotient contributes either \((a,\text{rank}_5)=(0,1)\) or \((1,0)\), giving the claimed formula for all smooth parameters.

**Exact pairwise-locus elimination.** Direct polynomial subtraction in \(\mathbb F_5[r,s,t]\) gives
\[
\begin{aligned}
H_1-H_2&=-2(r^2+1)(t^2-s^2),\\
H_1-H_3&=-2(t^2+1)(r^2-s^2),\\
H_2-H_3&=-2(s^2+1)(r^2-t^2).
\end{aligned}
\]
On the smooth locus, \(r^2+1\), \(s^2+1\), \(t^2+1\) are nonzero because \(4=-1\). Hence \(H_1=H_2=0\) forces \(t=s\) or \(t=-s\). The two substitutions factor exactly as
\[
\begin{aligned}
H_1(r,s,s)&=(r-2)((r+2)-2s^2(r+1)),\\
H_1(r,s,-s)&=(r+2)((r-2)-2s^2(r-1)).
\end{aligned}
\]
Since \(r=\pm2\) is singular, the only smooth solutions are \(r=f(s),t=s\) and \(r=-f(s),t=-s\). The denominator \(2s^2-1\) cannot vanish at any solution of either remaining linear equation (its constant term is then nonzero). The exclusion \(s=0\) is forced by \(r^2-4=0\). Cyclic permutation gives all six and no other pairwise loci.

**Smoothness and rationality of the six curves.** Put \(N=2-2u^2\) and \(D=2u^2-1\). In characteristic five the exact identities
\[
N^2-4D^2=-2u^2(u^2-4),\quad
N^2+2u^2D^2-Nu^2D-4D^2=2u^2(u^2-4)^2
\]
show that, after substituting \((r,s,t)=(\pm N/D,u,\pm u)\) with equal choices of sign, both \(r^2-4\) and the final smoothness factor are nonzero precisely on \(U\); the factors \(s^2-4\) and \(t^2-4\) are nonzero there as well. Each graph has a regular inverse given by projection to \(s=u\), so is an irreducible smooth rational curve isomorphic to \(U\). The two graphs for one Hasse pair are disjoint on \(U\), since \(s\ne0\). The cyclically permuted graphs cover the other pairs.

**Triple intersections and exhaustive incidence.** Simultaneously vanishing \(H_1,H_2,H_3\) forces \(r^2=s^2=t^2=q\) by the three difference identities. Inserting these squares into any \(H_i\) gives \(rst=q^2+2\). Since \((rst)^2=q^3\), this is possible if and only if
\[
(q^2+2)^2-q^3=(q+1)^2(q^2+2q-1)=0.
\]
The root \(q=-1=4\) is excluded by smoothness. The quadratic \(q^2+2q-1\) has two distinct nonzero roots, neither equal to \(4\). Each has four sign choices of \((r,s,t)\) with the required product, yielding exactly eight smooth triples (the final smoothness factor is nonzero, since it equals \(3q-q^2-6\), which on the quadratic roots simplifies to \(5q-7=-7\ne0\)). Each triple belongs to one component from each Hasse pair, and any cross-pair component intersection is necessarily one of these triples. Equivalently, the four triple parameters on each graph are certified by
\[
N^2-u^2D^2=(u^2-4)(u^2+2u-2)(u^2-2u-2).
\]
The two nonboundary quadratic factors have four distinct admissible roots. This proves exhaustiveness over the algebraic closure.

## Verification
Run `python3 verify.py` using only the Python standard library. The supplied program compares complete polynomial coefficient dictionaries over \(\mathbb F_5\) for each pairwise Hasse difference, graph factorization, boundary discriminant identity, third Hasse factorization, and triple-point equation. As a supplementary finite check it exhaustively enumerates all \(5^3=125\) coefficient triples defined over \(\mathbb F_5\): among 23 smooth triples, eleven have \(a=0\) and twelve have \(a=2\). These finite counts are **not** used as proofs about the algebraic closure; the identities above supply the geometric completeness argument.

## Relationship to prior work
Ohashi's *On the maximality of genus-3 nonhyperelliptic curves of Ciani type* (2022), in Sections 2–4, proves the smoothness criterion, gives the three elliptic quotients and their prime-to-characteristic isogeny, and proves maximality/minimality assertions **assuming** superspeciality. It cites Brock's earlier superspecial Ciani enumeration. None of the inspected assertions determines the full \(a\ge2\) stratum with six rational components and their eight triple incidences. Ohashi–Kudo–Harashita's paper on genus-three curves with cyclic automorphism group of order six instead computes \(a\)-numbers for a distinct one-parameter family. Its introduction explicitly notes that quotient-elliptic descriptions are known for other automorphism types; the new step here is the elimination and geometric classification of intermediate rank-one parameters, not rediscovery of that decomposition.

## Limitations
The classification is for labelled coefficients \((r,s,t)\) in characteristic five, restricted to smooth quartics. Permutation/sign and further geometric isomorphisms may identify parameters; no moduli-quotient counts are claimed. The eight superspecial parameter points are **not** claimed to be new as an isomorphism-class enumeration. Priority remains conditional on the inspected literature; an unindexed or differently parametrized earlier stratification is a residual risk. The arithmetic enumeration over \(\mathbb F_5\) does not establish geometric completeness without the symbolic proof above.

## References
1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1 (31 January 2022), Sections 2–4; https://arxiv.org/html/2201.12996v1 .
2. R. Ohashi, M. Kudo and S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777v3, introduction and Section 3; https://arxiv.org/html/2111.09777v3 .
3. Brock, *Superspecial curves of genera two and three*, 1993, Theorem 3.15 (as referenced in [1]); superspecial enumeration context only.
