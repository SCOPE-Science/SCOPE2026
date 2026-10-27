# The interval intersection lattice of the nilpotent Witt commuting variety

## Finding
Let \(k\) be algebraically closed of characteristic \(p>3\), with \(p\) prime. Let \(W=\operatorname{Der}_k(k[x]/(x^p))\) and \(\mathcal N=\{D\in W:D^{[p]}=0\}\). Write the irreducible components of the commuting variety \(\mathcal C(\mathcal N)=\{(D,E)\in\mathcal N^2:[D,E]=0\}\) as \(C_0,\ldots,C_m\), where \(m=(p-3)/2\), using the intrinsic filtration labels in [1].

**Intersection theorem.** For every nonempty \(S\subseteq\{0,\ldots,m\}\), put \(a=\min S\) and \(b=\max S\). Then the *reduced, set-theoretic* component intersection depends only on \((a,b)\):
\[
\bigcap_{i\in S}C_i=C_a\cap C_b,\qquad
\dim(C_a\cap C_b)=p+a-b.
\]
If \(a\ge1\), it is isomorphic, as a reduced variety, to \(\mathbb A^{2a}_k\times\{M\in\operatorname{Mat}_{2\times(p-1-a-b)}(k):\operatorname{rank}M\le1\}\). If \(a=0<b\), it is the same rank-at-most-one determinantal cone without an affine factor; for \(a=b=0\), it is the irreducible variety of dependent pairs of nilpotent Witt elements. Every component has dimension \(p\). Consequently the codimension-one intersection graph on these components is precisely the path \(C_0-C_1-\cdots-C_m\).

All these varieties and their identifications are defined over \(\mathbb F_p\). For every \(q=p^e\), \(e\ge1\), there is also an exact *simultaneous-intersection* point count, including the singleton case:
\[
\left|\left(\bigcap_{i\in S}C_i\right)(\mathbb F_q)\right|
=q^{2a}\bigl(1+(q+1)(q^{p-1-a-b}-1)\bigr).
\]

## Assumptions and scope
The filtration is \(\mathfrak g_i=x^{i+1}k[x]/(x^p)\,\partial_x\) for \(0\le i\le p-2\), and \(\mathfrak g_{p-1}=0\). The component \(C_i\) for \(i\ge1\) is the closure of the commuting-pair stratum with its first coordinate in \(\mathfrak g_i\setminus\mathfrak g_{i+1}\), as in [1]. The component \(C_0\) is the closure of the first-coordinate stratum of nonzero constant coefficient. All intersections below mean intersections of their underlying *reduced varieties*, not claims that the scheme-theoretic sum of component ideals is radical. The formula also counts the resulting geometrically defined loci over all finite extensions \(\mathbb F_q\) of the prime field.

## Proof
**1. Centralizers.** Identify \(f\partial_x\in W\) with its truncated coefficient polynomial \(f\). The bracket is \([f\partial_x,g\partial_x]=(fg'-gf')\partial_x\). Fix \(1\le i\le m\), and write \(r=i+1\), \(\ell=p-1-i\). If \(f\in\mathfrak g_i\setminus\mathfrak g_{i+1}\), then \(\operatorname{ord}_x(f)=r\). Comparing the first nonzero coefficient of \(fg'-gf'\) shows that for a centralizing \(g\), if its least exponent \(s\le p-r\), necessarily \(s=r\): otherwise the coefficient at exponent \(r+s-1<p\) is \((s-r)f_rg_s\ne0\). Indeed \(0<|s-r|<p\). Subtracting \((g_r/f_r)f\) then forces the remainder to have order at least \(p-r+1\); conversely all such remainders centralize \(f\) because both terms of their bracket have degree at least \(p\). Thus
\[
\operatorname{Cent}_W(f\partial_x)=k(f\partial_x)\oplus\mathfrak g_{\ell}.
\]
This also reproves the relevant centralizer statement in [1] in the current normalization.

**2. Determinantal equations for complete component closures.** For \(i\ge1\) set
\[
P_i=\{(f,g)\in\mathfrak g_i^2:\dim_k\langle f+\mathfrak g_{\ell_i},g+\mathfrak g_{\ell_i}\rangle\le1\},\quad\ell_i=p-1-i.
\]
Equivalently every \(2\times2\) minor of the two coefficient rows of exponents \(i+1,\ldots,p-1-i\) vanishes. The \(2i\) remaining high-degree coefficients are free, so \(P_i\cong\mathbb A_k^{2i}\times D_{2,p-1-2i}\), where \(D_{2,d}\) is the determinantal cone of \(2\times d\) matrices of rank at most one. This is irreducible of dimension \(2i+(p-1-2i)+1=p\). The open part where the leading coefficient of \(f\) is nonzero is precisely \(g=cf+h\), \(h\in\mathfrak g_{\ell_i}\), by Step 1; it is dense in \(P_i\). Therefore \(C_i=P_i\), not only inclusion or equality on a dense open set.

For \(i=0\), the generic centralizer is the line spanned by its first-coordinate element (this also follows from \((g/f)'=0\) when \(f(0)\ne0\)). Nilpotency of \(f\) forces nilpotency of any multiple; taking closure gives
\[
C_0=\{(f,g)\in\mathcal N^2:\dim_k\langle f,g\rangle\le1\}.
\]
The reversed-coordinate locus \((0,g)\) is obtained as the limit of \((tf,g)\) with \(f=g\) and \(t\to0\); hence no extra component is being discarded.

**3. All intersections.** If \(1\le a<b\), then \(\mathfrak g_{\ell_a}\subset\mathfrak g_{\ell_b}\). On \(\mathfrak g_b^2\), proportionality modulo \(\mathfrak g_{\ell_a}\) implies proportionality modulo \(\mathfrak g_{\ell_b}\). Hence \(P_a\cap P_b=P_a\cap\mathfrak g_b^2\), and after separating the \(2a\) free coordinates in \(\mathfrak g_{\ell_a}^2\), this is \(\mathbb A^{2a}\times D_{2,p-1-a-b}\). The same implication holds for every \(a<j<b\), establishing the interval property. If \(a=0<b\), proportionality in \(W\) plus the condition \((f,g)\in\mathfrak g_b^2\) is exactly the rank-one cone \(D_{2,p-1-b}\); all its elements are nilpotent because \(\mathfrak g_b\subseteq\mathfrak g_1\), and every intermediate \(P_j\) contains it. For \(a=b=0\) use Step 2 directly. For all cases the displayed dimension is \(2a+(p-1-a-b)+1=p+a-b\). Since every \(C_i\) has dimension \(p\), a distinct pair meets in a divisor of both components precisely when \(b-a=1\); this proves the path assertion.

**4. Finite-field counts and the exceptional first component.** The rank-one cone \(D_{2,d}\) has \(1+(q+1)(q^d-1)\) \(\mathbb F_q\)-points: for a nonzero matrix the row-space is a unique line of \(\mathbb F_q^2\), with \(q+1\) choices, and the remaining nonzero vector has \(q^d-1\) choices. Step 3 supplies the power \(q^{2a}\). It remains to count \(C_0\). One has \(|\mathcal N(\mathbb F_q)|=q^{p-1}\): if \(f(0)=0\), then \(f\partial_x\) is \(p\)-nilpotent exactly when its linear coefficient vanishes, giving \(q^{p-2}\) choices. If \(f(0)\ne0\), its centralizer in \(W\) is the line it spans, so \((f\partial_x)^p=\lambda(f\partial_x)\); the coefficient of its top term \(x^{p-1}\) enters \(\lambda\) affinely, with nonzero coefficient \((p-1)!f(0)^{p-2}\). Thus for any choice of the lower \(p-1\) coefficients with \(f(0)\ne0\) there is exactly one top coefficient making \(\lambda=0\), accounting for \((q-1)q^{p-2}\) more elements. (The nonzero coefficient follows by applying the derivation \(p\) times to \(x\); the term linear in the top coefficient occurs exactly once and applies the constant derivation in the other \(p-1\) steps.) The set of dependent pairs of nilpotents therefore has \(1+(q+1)(q^{p-1}-1)\) points, by the same projective-line count. This is the displayed formula for \(a=b=0\).

## Verification
The self-contained file `witt_component_intersection_checker.py` tests the bracket and all component determinantal conditions over prime fields. It exhaustively examines \(15{,}625\) ordered pairs in the high-degree slice for \(p=5\) (including the common intersection with \(C_0\)) and carries out seeded randomized implication and commuting-locus tests for \(p=7\) and \(p=11\). Running `python3 witt_component_intersection_checker.py` returns `WITT_INTERSECTIONS_OK`. These are finite checks only; the proof above establishes arbitrary \(p>3\) and all corresponding finite extensions.

## Relationship to prior work
Yao and Chang [1] prove the irreducible-component decomposition of the nilpotent Witt commuting variety, including the component labels, common dimension, and centralizer stratification. The present result determines the complete *higher intersection lattice*, reduced determinantal geometry of every nontrivial intersection, its codimensions, the path dual graph, and its extension-field rational-point counts. Those conclusions require extending the dense-stratum description to explicit global determinantal equations and comparing such equations across filtrations; they are not statements of [1]. Chang and Yao [2] address rational nilpotent orbits and nilpotent counting, not intersections of commuting-variety components. Yao [3] studies commuting \(r\)-tuple components; only its abstract was accessible for comparison, so possible stronger unpublished or published overlap remains a real limitation.

## Limitations
The results refer to reduced intersections, not possible nonreduced scheme-theoretic intersection structures. No singularity, multiplicity, or cohomology classification is claimed. The proof covers the restricted one-variable Witt algebra in characteristic \(p>3\), not general Cartan-type Lie algebras. Checks for small prime fields cannot certify the theorem without the argument above. Global novelty is not certified; the unavailable full text of [3] leaves residual overlap risk.

## References
[1] X. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667 (first public version, 2013-01-23), https://arxiv.org/abs/1301.5667 .

[2] H. Chang and X. Yao, *On F_q-Rational Structure of Nilpotent Orbits in Witt Algebra*, DOI:10.1007/s00025-013-0339-1 (2014).

[3] X. Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, Journal of Pure and Applied Algebra (2015), DOI:10.1016/j.jpaa.2015.02.005 (abstract inspected; full text not available for comparison).
