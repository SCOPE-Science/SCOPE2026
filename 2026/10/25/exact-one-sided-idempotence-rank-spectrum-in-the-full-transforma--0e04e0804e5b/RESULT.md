# Exact one-sided idempotence rank spectrum in the full transformation monoid

## Finding

Let \(n\ge1\), let \(X\) be a labeled set of \(n\) points, and let \(\mathcal T_X\) be the monoid of all total maps \(X\to X\). Composition is \(ef=e\circ f\), so \(f\) acts first. For integers \(r,s,t\), put
\[
N_n(r,s,t)=\#\{(e,f)\in\mathcal T_X^2:
e^2=e,\ f^2=f,\ (ef)^2=ef,\
\operatorname{rank}(e)=r,\
\operatorname{rank}(f)=s,\
\operatorname{rank}(ef)=t\}.
\]
If \(1\le r,s\le n\), \(1\le t\le\min(r,s)\), and \(L=n-r-s+t\ge0\), then
\[
\boxed{
N_n(r,s,t)=
\frac{n!\,s^{r-t}t^{s-t}}{t!(r-t)!(s-t)!}
\sum_{j=0}^{\min(t,L)}
\binom tj\frac{(rs)^{L-j}}{(L-j)!}.
}
\]
In every other case \(N_n(r,s,t)=0\). Every triple satisfying the displayed inequalities actually occurs. This formula includes noncommuting pairs of idempotents: it is not a commuting-pair formula.

An equivalent one-parameter exponential-generating-function description is
\[
\boxed{
\sum_{n,r,t\ge0}
\left(\sum_{\substack{e^2=e,\ f^2=f,\ (ef)^2=ef\\
\operatorname{rank}(e)=r,\ \operatorname{rank}(f)=s\\
\operatorname{rank}(ef)=t}}1\right)
\frac{z^n}{n!}u^r v^t
=
[x^s]\exp\!\left(
u\left(sz e^{sz}+v xz(1+z)e^{(s+x)z}\right)
\right).
}
\]
For this identity \(s\ge1\) is fixed; on the left the maps act on labeled \(n\)-sets and \(n\ge0\). The fixed-positive-rank coefficient is zero at \(n=0\).

## Assumptions and scope

A map is idempotent precisely when it fixes every point in its image. The ranks are cardinalities of images. Every e-idempotent has a unique partition into nonempty kernel fibers \(P_a=e^{-1}(a)\), each with one distinguished anchor \(a\in P_a\). Conversely a set of rooted blocks specifies an e-idempotent. The result counts **ordered labeled pairs**, without simultaneous-conjugacy quotienting. No commutativity of \(e\) and \(f\) is assumed. The ambient set is finite and nonempty, and all formulas are exact integers.

## Proof

**Step 1 (the product-idempotence criterion).**
Fix \(e^2=e\), write \(A=\operatorname{im}(e)\), and write the fibers as \(P_a=e^{-1}(a)\) for \(a\in A\). Fix \(f^2=f\) and let \(B=\operatorname{im}(f)\) be its set of fixed roots, with \(|B|=s\). Since \(ef(X)=e(B)\), its image rank is exactly the number \(t\) of \(e\)-fibers meeting \(B\).

A transformation \(h\) is idempotent if and only if \(h\) fixes its image pointwise. Thus \(ef\) is idempotent if and only if
\[
f(a)\in P_a\quad\text{for every }a\in A
\text{ such that }P_a\cap B\ne\varnothing.
\]
If \(a\in B\), this holds automatically. If \(a\notin B\) but the fiber meets \(B\), then \(f(a)\) must be chosen from \(B\cap P_a\). If \(B\cap P_a=\varnothing\), the value \(f(a)\) can be any one of the \(s\) roots in \(B\). Every nonroot \(x\notin B\) other than these constrained anchors also maps freely into \(B\). These conditions are necessary and sufficient, with no coupling left between different fibers once \(B\) is chosen.

**Step 2 (the reversible rooted-block count).**
Use \(z\) for each labeled point, \(u\) for each \(e\)-fiber, \(x\) for each \(f\)-root, and \(v\) for each \(e\)-fiber that meets \(B\). The total number of \(f\)-roots is the fixed external parameter \(s\). A rooted \(e\)-fiber admits exactly three mutually exclusive types, each with its exponential weight:

* The fiber has no \(f\)-root. Its \(e\)-anchor and all other points map under \(f\) to one of \(s\) global \(f\)-roots: \(sz e^{sz}\).
* The fiber contains its own anchor among its \(f\)-roots. This anchor is fixed by \(f\); each other point is either an \(f\)-root or has one of \(s\) possible \(f\)-images: \(v xz e^{(s+x)z}\).
* The fiber meets \(B\) but its anchor is not an \(f\)-root. The anchor must choose one of the \(f\)-roots among the other points of that same fiber. Pointing at that root contributes the factor \(xz\), while the anchor contributes \(z\): \(v xz^2e^{(s+x)z}\).

Conversely, every labeled set of blocks made from these three types defines a unique admissible pair \((e,f)\), because roots of \(f\) are precisely the \(x\)-marked vertices and the remaining vertices have their indicated choices of \(f\)-images. The exponential formula for a set of rooted blocks consequently gives
\[
\Phi_s(z,u,x,v)
=\exp\!\left(u\bigl(sz e^{sz}+v xz(1+z)e^{(s+x)z}\bigr)\right).
\]
Hence \(N_n(r,s,t)=n![z^n u^r x^s v^t]\Phi_s\).

**Step 3 (coefficient extraction).**
Selecting exactly \(r-t\) unoccupied and \(t\) occupied \(e\)-fibers gives
\[
[u^r v^t]\Phi_s
=
\frac{s^{r-t}x^tz^r(1+z)^t
 e^{rsz}e^{txz}}{(r-t)!t!}.
\]
Taking the \(x^s\) coefficient in the final exponential contributes
\[
[x^{s-t}]e^{txz}
=\frac{t^{s-t}z^{s-t}}{(s-t)!}.
\]
The remaining coefficient is
\[
[z^L](1+z)^t e^{rsz}
=\sum_{j=0}^{\min(t,L)}
\binom tj\frac{(rs)^{L-j}}{(L-j)!},
\qquad L=n-r-s+t.
\]
This proves the stated closed expression with its factorial factors and composition convention.

**Step 4 (exact support).**
Every nonempty finite total-map image has positive rank, and each occupied \(e\)-fiber contains at least one \(f\)-root, so \(1\le t\le\min(r,s)\). The smallest possible total number of points supporting \(r\) rooted \(e\)-fibers and \(s\) \(f\)-roots distributed over \(t\) occupied fibers is \(r+s-t\). Conversely, for every permitted \((n,r,s,t)\), create \(r\) rooted fibers, put one \(f\)-root in each of \(t\) selected fibers, put the remaining \(s-t\) \(f\)-roots in those selected fibers, and distribute \(n-r-s+t\) extra points arbitrarily; the choices in Step 1 give an admissible pair. Alternatively, the closed formula is strictly positive for these parameters. All asserted boundaries therefore follow.

## Verification

The standalone standard-library script `verify.py` constructs all idempotent self-maps as value vectors and tests actual compositions, independently of the rooted-block encoding. It checks **every rank triple** for \(1\le n\le6\), with total qualifying pair counts
\[
1,\ 9,\ 94,\ 1417,\ 28856,\ 746179.
\]
For \(1\le n\le4\), a second procedure independently counts admissible maps by fixing an \(e\)-idempotent and summing over candidate \(f\)-root sets. The script also tests the support boundary and exact formula for all \(1\le n\le14\). Run `python3 verify.py` using Python's standard library. Its terminal marker is `VERIFY_OK_IDEMPOTENT_PRODUCT_RANK_TRIPLES`.

These are finite checks of a universal proof, not exhaustive proof by enumeration.

## Relationship to prior work

Blyth and Almeida Santos studied **skew pairs** of idempotents in full transformation semigroups, where just one ordering of the two products is idempotent; their accessible abstract concerns existence and types, rather than the joint factor/product rank count. Their full paper was not available for direct comparison here. Gray and Ruškuc analyzed the biordered set of idempotents in the full transformation monoid and associated maximal subgroups, using kernel partitions and image transversals, but the inspected introduction, normal-form section, and searched PDF text did not supply the displayed one-sided idempotence distribution. Luangchaisri and Changphas studied existence of skew pairs in **partial** transformation semigroups; their inspected results likewise concern existence thresholds and skew-pair types.

Commuting idempotents are a proper subset of the present pairs. For example, on three points there are \(94\) ordered idempotent pairs with idempotent product, whereas direct enumeration gives \(58\) commuting ordered idempotent pairs. Hence a formula for commuting idempotents alone does not imply this count. No equivalence with the published statements inspected was identified, but absence from inspected sources is not a priority proof.

## Limitations

The finding concerns products of **two total idempotent maps** on a finite labeled set. It does not enumerate factorization fibers for each individual product, distinguish all four skew-pair types, or extend to arbitrary partial transformations or products of three or more factors. The full 2006 skew-pair paper could not be examined; historical precedence of an equivalent rank-triple formula remains a specific risk. The mathematical argument and computational checks were not independently audited.

## References

1. R. Gray and N. Ruškuc, *Maximal subgroups of free idempotent generated semigroups over the full transformation monoid*, arXiv:1101.1833v1, publicly submitted 2011-01-10, https://arxiv.org/abs/1101.1833.
2. T. S. Blyth and M. H. Almeida Santos, *Skew pairs of idempotents in transformation semigroups*, Acta Mathematica Sinica 22 (2006), 1705–1714, DOI:10.1007/s10114-005-0703-5; institutional preprint catalog (2005, day unspecified), https://www.dm.fct.unl.pt/en/investigacao/pre-publicacoes/2005/skew-pairs-idempotents-transformation-semigroups.
3. P. Luangchaisri and T. Changphas, *Skew Pairs of Idempotents in Partial Transformation Semigroups*, Mathematics 10 (2022), article 2, first public 2021-12-21, DOI:10.3390/math10010002.
4. J. M. Howie, *Products of idempotents in finite full transformation semigroups: some improved bounds*, Proc. R. Soc. Edinburgh A 98 (1984), 25–35, DOI:10.1017/S0308210500025531.
