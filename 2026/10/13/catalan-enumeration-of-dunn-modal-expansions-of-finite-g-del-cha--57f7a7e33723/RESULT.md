# Catalan enumeration of Dunn modal expansions of finite Gödel chains

## Finding

Let \(C_m=\{0<1<\cdots <m-1}\) be the nontrivial \(m\)-element Gödel chain, \(m\ge2\). Flaminio, Godo, Menchón, and Rodriguez define a Gödel algebra with operators (GAO) by requiring \(\Box\) to preserve \(1\) and binary meets and \(\Diamond\) to preserve \(0\) and binary joins; their Dunn subvariety additionally satisfies
\[
\Box(aee b)\le \Box aee\Diamond b,
\qquad
\Box a\wedge\Diamond b\le\Diamond(a\wedge b).
\]
For a chain these axioms admit a complete classification:
\[
oxed{	ext{either }\Box\equiv1,\ \Diamond\equiv0,\quad	ext{or}\quad
\Box,\Diamond	ext{ fix }0,1	ext{ and }\Box x\le\Diamond x	ext{ for every }x.}
\]
In the second case the two maps are precisely bounded-lattice endomorphisms of the chain with pointwise order \(\Box\le\Diamond\).

It follows that the exact number of Dunn GAO expansions of \(C_m\) is
\[
oxed{N_m=1+(2m-3)\,\mathrm{Cat}_{m-2}\mathrm{Cat}_{m-1}},
\qquad
\mathrm{Cat}_n=rac1{n+1}inom{2n}{n}.
\]
Because a finite chain has no nonidentity lattice automorphism, this is also the number of isomorphism types. The first values are
\[
N_2,N_3,N_4,N_5,N_6=2,7,51,491,5293.
\]
Asymptotically, \(N_m\sim 16^m/(32\pi m^2)\).

## Assumptions and scope

The result concerns expansions of the fixed finite Gödel chain \(C_m\), not arbitrary finite Gödel algebras or arbitrary positive modal algebras. The terminology and Dunn axioms are those of Flaminio--Godo--Menchón--Rodriguez. Their paper explicitly restricts its algebraic development to finite Gödel algebras and gives the GAO equations and Dunn equations used here.

The one-element chain is degenerate and has a unique expansion; the displayed Catalan formula is stated for \(m\ge2\).

## Proof

On a finite chain, a unary map preserves binary meets exactly when it is monotone, and it preserves binary joins exactly when it is monotone. Hence a GAO expansion of \(C_m\) is equivalently a pair of monotone maps \(b=\Box\) and \(d=\Diamond\) such that \(b(1)=1\) and \(d(0)=0\).

First suppose \(d(1)<1\). In Dunn axiom (D1), put the second argument equal to \(1\). For every \(a<1\),
\[
1=b(1)=b(aee1)\le b(a)ee d(1).
\]
Since \(d(1)<1\) and the algebra is a chain, this forces \(b(a)=1\). Thus \(b\equiv1\). Now (D2) with \(a=0\) and the second argument \(1\) gives
\[
d(1)=b(0)\wedge d(1)\le d(0)=0,
\]
so \(d(1)=0\), and monotonicity yields \(d\equiv0\). This is the unique exceptional expansion.

Now suppose \(d(1)=1\). Taking the second argument of (D2) to be \(1\) gives, for every \(a\),
\[
b(a)=b(a)\wedge d(1)\le d(a),
\]
so \(b\le d\) pointwise. In particular \(b(0)=0\); together with the endpoint conditions, both maps fix \(0\) and \(1\). Conversely, let \(b,d\) be monotone, fix both endpoints, and satisfy \(b\le d\). If \(a\ge c\), then (D1) is immediate because its right side contains \(b(a)\); if \(c\ge a\), then \(b(c)\le d(c)\). Similarly, if \(a\le c\), then the left side of (D2) is at most \(b(a)\le d(a)\), while if \(c\le a\) it is at most \(d(c)\). Hence both Dunn axioms hold. This proves the classification.

It remains to count the normal expansions. Their internal values form two weakly increasing sequences
\[
0=b_0\le b_1\le\cdots\le b_{m-2}\le b_{m-1}=m-1,
\]
\[
0=d_0\le d_1\le\cdots\le d_{m-2}\le d_{m-1}=m-1,
\qquad b_i\le d_i.
\]
Reverse the \(m-2\) internal coordinates and put the \(d\)-row above the \(b\)-row. This is exactly a plane partition in a \(2	imes(m-2)	imes(m-1)\) box. MacMahon's box formula therefore gives
\[
\prod_{i=1}^2\prod_{j=1}^{m-2}
rac{i+j+m-2}{i+j-1}
=
rac{(2m-3)!(2m-2)!}{(m-2)!(m-1)!^2m!}
=(2m-3)\mathrm{Cat}_{m-2}\mathrm{Cat}_{m-1}.
\]
Adding the exceptional expansion gives \(N_m\). The asymptotic follows from \(\mathrm{Cat}_n\sim4^n/(\sqrt\pi n^{3/2})\).

## Verification

The bundled exact replay enumerates every monotone \(\Box\) with \(\Box1=1\) and every monotone \(\Diamond\) with \(\Diamond0=0\) for \(2\le m\le6\), tests both Dunn inequalities on every ordered pair of chain elements, and verifies that every passing pair belongs to exactly one of the two classes above. It recovers the counts

```text
2 2 2
3 7 7
4 51 51
5 491 491
6 5293 5293
```

where each row is `m exhaustive_count formula_count`. It also checks the MacMahon-product simplification for \(2\le m\le30\). Expected terminal line:

```text
VERIFY_OK ... exact assertions/comparisons
```

## Relationship to prior work

Flaminio--Godo--Menchón--Rodriguez introduce GAOs, state the four operator equations, and define Dunn GAOs by (D1) and (D2). They develop dual forest representations and characterize the frame effect of the Dunn equations. Their text does not enumerate chain expansions; targeted full-text searches found no occurrence of “Catalan,” “number of,” or “finite chain.”

Candidate-specific searches were run in published-finding corpus under Dunn-GAO, finite-Gödel-chain, Catalan, modal-operator, and pointwise-monotone formulations. Exact web searches included the count sequence \(2,7,51,491,5293\), the Catalan product, and broader positive-modal-algebra chain terminology. No equivalent classification or enumeration was located. The current and preceding owned cumulative ledgers were also checked for the same formulations and contained no equivalent finding.

The nearest broader literature concerns representation/duality for positive modal algebras and structural results for positive modal varieties; those works establish the ambient algebraic setting rather than this finite-chain census.

## Limitations

This is a same-model derivation and verification, not an independently audited result. The literature search cannot exclude uncatalogued folklore, lecture notes, or an enumeration stated under substantially different terminology. The formula is specific to chains; branching Gödel algebras need not reduce to two pointwise ordered monotone maps.

## References

1. T. Flaminio, L. Godo, P. Menchón, R. O. Rodriguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528 (first public version 6 October 2021); later in *Many-valued Semantics and Modal Logics*, Synthese Library 485, Springer, 2024, pp. 179--216, DOI:10.1007/978-3-031-56595-3_7.
2. J. M. Dunn, *Positive modal logic*, Studia Logica 55 (1995), 301--317, DOI:10.1007/BF01061239.
