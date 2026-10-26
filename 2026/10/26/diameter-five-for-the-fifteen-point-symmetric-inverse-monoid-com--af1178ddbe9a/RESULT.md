# Diameter five for the fifteen-point symmetric inverse monoid commuting graph

## Finding
Let \(X=\{0,1,\ldots,14\}\) and let \(\mathcal I(X)\) be the symmetric inverse monoid of partial bijections, including the empty map \(0\) and identity \(1\). The commuting graph \(\mathcal G(\mathcal I(X))\) has vertex set \(\mathcal I(X)\setminus\{0,1\}\), and distinct vertices are adjacent exactly when they commute under composition.

**Theorem.** The diameter is exactly
\[
\operatorname{diam}\mathcal G(\mathcal I(X))=5.
\]
This resolves the first odd composite size divisible by two distinct prime factors left at the alternatives \(4\) and \(5\) by Araújo–Bentz–Konieczny (2012), Proposition 6.13.

More precisely, let \(\alpha(i)=i+1\pmod{15}\) and let \(\beta\) be the permutation whose images, in input order \(0,1,\ldots,14\), are
```
[12, 7, 8, 14, 5, 2, 0, 3, 6, 13, 4, 1, 9, 11, 10]
```
Then \(\alpha\) and \(\beta\) are fifteen-cycles at distance exactly five.

## Assumptions and scope
We use ordinary right-to-left function composition; \(fg=f\circ g\). All maps are on the displayed fifteen-point set. The graph excludes its two central elements, the empty map and identity. The claim concerns the entire inverse monoid, not merely its unit group. Its sole external input is the published upper bound from Proposition 6.13, which applies to every odd composite size.

## Proof
**Upper bound.** Proposition 6.13(2) of Araújo–Bentz–Konieczny gives diameter at most \(5\) for every odd composite size; thus for \(15\).

**Neighbors of full cycles.** Suppose a partial injection \(\gamma\) commutes with an \(n\)-cycle \(\sigma\). Its domain is \(\sigma\)-invariant, so empty or full. In the latter case it is a permutation, and commutation with a full cycle implies \(\gamma=\sigma^i\). Therefore every graph neighbor of \(\alpha\), respectively \(\beta\), equals a nonidentity power of that cycle.

**Four finite centralizer certificates.** Direct calculations using the displayed permutations establish the following table. In each row \(H=\langle\alpha^i,\beta^j\rangle\); the second column is the size of the orbit of \(0\) under \(H\), and the third lists all images \(\tau(0)\) possible for a permutation \(\tau\) commuting with both generators.

| \((i,j)\) | \(|H\cdot0|\) | admissible \(\tau(0)\) |
| --- | ---: | --- |
| \((3,3)\) | \(15\) | \(\{0\}\) |
| \((3,5)\) | \(15\) | \(\{0\}\) |
| \((5,3)\) | \(15\) | \(\{0\}\) |
| \((5,5)\) | \(15\) | \(\{0\}\) |

Here the finite calculation is itself exhaustive: for each of the four rows and each of the fifteen candidate images of \(0\), assign \(\tau(0)=t\); propagate \(\tau(gv)=g\tau(v)\) for both generators and their inverses, checking consistency and injectivity. Transitivity reaches every point, so the assignment uniquely determines any possible centralizing permutation. The accompanying pure-Python program performs every propagation and verifies each assertion, as well as an independent check of all \(196\) pairs of nonidentity powers. The listed data are exact finite certificates, not statistical tests.

For arbitrary \(1\le r,s\le14\), any map commuting with both \(\alpha^r\) and \(\beta^s\) also commutes with some \(\alpha^i\), \(i\in\{3,5\}\), and some \(\beta^j\), \(j\in\{3,5\}\): a nonidentity power of a fifteen-cycle has order \(3\), \(5\), or \(15\), and contains a nonidentity power of order \(3\) or \(5\). Consequently, by the four certificates, \(\langle\alpha^r,\beta^s\rangle\) is transitive and has trivial centralizer in \(S_{15}\). A partial injection commuting with this transitive group has invariant domain, hence domain either empty or full; in the full case it is one of the centralizing permutations, hence the identity. Therefore **the only common centralizers in the inverse monoid** of \(\alpha^r\) and \(\beta^s\) are \(0\) and \(1\).

**Lower bound.** If a graph path of length at most four joined \(\alpha\) to \(\beta\), insert repetitions as needed to express its commuting relations as \(\alpha\sim\delta\sim\gamma\sim\eta\sim\beta\), where \(\delta\), \(\gamma\), \(\eta\) are noncentral vertices (the relation \(\sim\) here permits equal adjacent entries for padding). By the full-cycle neighbor property, \(\delta=\alpha^r\) and \(\eta=\beta^s\) for some \(1\le r,s\le14\). The middle vertex \(\gamma\) would be a noncentral common centralizer, contradicting the preceding paragraph. Thus \(d(\alpha,\beta)\ge5\).

**Explicit five-edge path.** Put \(A=\{0,5,10\}\), \(B=\{2,3,9\}\), and denote by \(e_A,e_B\) the partial identities on these disjoint sets. The set \(A\) is an \(\alpha^5\)-orbit, and \(B\) is a \(\beta^5\)-orbit. Therefore
\[
\alpha\;\text{--}\;\alpha^5\;\text{--}\;e_A\;\text{--}\;e_B\;\text{--}\;\beta^5\;\text{--}\;\beta
\]
is a legitimate path of five edges. This and the upper bound complete the proof.

## Verification
Run `python3 verify.py` using Python 3 and no third-party packages. It checks both fifteen-cycles; verifies the four exhaustive image-propagation certificates; independently checks all \(14^2=196\) power-pair centralizers and transitivity; and directly checks all five commuting edges of the path by composing partial maps. Expected terminal line: `VERIFY_OK_INVERSE_MONOID_15_DIAMETER_5`.

## Relationship to prior work
Araújo, Bentz, and Konieczny (2012), Proposition 6.13, bounded this graph's diameter by \(4\) or \(5\) for odd composite degree. Their Lemma 6.15 and Theorem 6.16 settled odd prime-power degrees, but not \(15\), whose factorization has two distinct primes. This result establishes the remaining lower bound in degree fifteen. Results on commuting graphs of the symmetric *group* do not directly give a lower bound in the symmetric inverse *monoid*, whose additional partial-injection vertices may shorten graph distances.

## Limitations
This is an exact finite-degree result for \(15\), not a proof for every odd degree divisible by distinct primes. The code is a finite exhaustive mathematical certificate; it is not a proof of claims for other degrees. A later or difficult-to-locate equivalent result remains possible; independent mathematical validation has not been performed.

## References
1. J. Araújo, W. Bentz, and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, first publicly posted 8 May 2012, arXiv:1205.1664, especially Proposition 6.13, Lemma 6.15, Theorem 6.16, and the closing discussion. https://arxiv.org/html/1205.1664v1
2. Same authors, *Israel Journal of Mathematics* 207 (2015), 103–149, DOI 10.1007/s11856-015-1173-9 (later journal version).
