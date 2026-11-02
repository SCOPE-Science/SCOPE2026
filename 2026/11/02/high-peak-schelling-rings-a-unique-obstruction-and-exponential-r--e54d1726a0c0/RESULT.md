# High-peak Schelling rings: a unique obstruction and exponential rarity of stable placements

## Finding

For every integer \(n\ge3\), let \(C_n\) be a cycle with \(b\) blue and \(r=n-b\) red occupants, where \(1\le b\le r\). In the fully occupied, two-type, strictly bilateral swap Schelling game with the single-peaked closed-neighborhood payoff of Bilò, Bilò, Lenzner and Molitor and any common peak \(1/2<\Lambda<1\), a placement is a swap equilibrium precisely when its circular binary word satisfies **both** conditions:

1. It contains no cyclic factor \(0101\) or \(1010\).
2. It does not simultaneously contain a cyclic \(000\) factor and a cyclic \(111\) factor.

Consequently an equilibrium exists for **every** admissible population split except \((n,b,r)=(6,3,3)\). The negative instance itself was known; the all-other-splits existence theorem and exact placement classification are the contributions here.

An exact labeled-vertex equilibrium count is given by the following finite transfer formula. Index three-bit words by \(s=(a,b,c)\in\{0,1\}^3\). For each exclusion set \(Q\subseteq\{000,111\}\), let the weighted \(8\times8\) matrix \(M_Q(u)\) have an entry \(u^d\) from \((a,b,c)\) to \((b,c,d)\) if \((a,b,c,d)\notin\{0101,1010\}\) and \((b,c,d)\notin Q\), and entry zero otherwise (summing weights if needed). Then the number of stable position-colorings with exactly \(b\) blue vertices, encoding blue as \(1\), is

\[
E_{n,b}=[u^b]\operatorname{tr}\big(M_{\{000\}}(u)^n+M_{\{111\}}(u)^n-M_{\{000,111\}}(u)^n\big).
\]

For instance \(E_{6,3}=0\), \(E_{7,3}=7\), \(E_{8,4}=20\), \(E_{10,5}=10\), and \(E_{12,6}=76\). All cycle positions are labeled; rotations and reflections are **not** identified. Same-type agents are interchangeable.

The total number \(S_n=\sum_{b=1}^{n-1}E_{n,b}\) of stable mixed-color placements obeys

\[
S_n\sim2\lambda^n,\qquad
\lambda=1.651736555\ldots,
\]

where \(\lambda\) is the Perron root of \(t^6-t^5-2t^3+1\). In particular, a uniformly chosen fair binary placement conditioned on both colors appearing is stable with probability

\[
\frac{S_n}{2^n-2}\sim2\left(\frac{\lambda}{2}\right)^n.
\]

Thus almost every population split admits a stable placement, yet a uniformly random placement is exponentially unlikely to be stable.

## Assumptions and scope

Vertices of the simple cycle are individually labeled \(0,\ldots,n-1\); for \(n=3\) this is the ordinary triangle. Every vertex has exactly two neighbors. A player has one of two fixed types and occupies one vertex; there are no vacancies. Its utility is \(p(f)\), where \(f\) is its own-type fraction among the player and its two neighbors. The payoff \(p:[0,1]\to[0,1]\) satisfies \(p(0)=0\), strict increase on \([0,\Lambda]\), \(p(\Lambda)=1\), and \(p(x)=p(\Lambda(1-x)/(1-\Lambda))\) for \(\Lambda\le x\le1\), with \(1/2<\Lambda<1\). Only **mutually strictly profitable** exchanges of two players are allowed. Equilibrium means no such exchange exists, not absence of unilaterally improving relocations.

Only three own-type fractions occur: \(1/3,2/3,1\). The payoff assumptions give \(p(2/3)>p(1/3)>p(1)=0\): if \(\Lambda\ge2/3\), strict increase on the lower branch proves this directly; if \(1/2<\Lambda<2/3\), the symmetry identity gives \(p(2/3)=p(\Lambda/[3(1-\Lambda)])\), and \(1/3<\Lambda/[3(1-\Lambda)]<\Lambda\). We may therefore replace the three numerical values by strict ordinal ranks \(2,1,0\), respectively; this normalization does not change any profitable swap.

## Proof

**Swap lemma.** Call a vertex *isolated* if its two neighbors have the opposite type; *boundary* if exactly one neighbor shares its type; *interior* if both neighbors share its type. The ordinal utilities of isolated, boundary and interior vertices are respectively \(1,2,0\). If opposite-type players at nonadjacent vertices exchange positions, each participant's number \(k\) of same-type neighbors becomes \(2-k\). Such an exchange strictly benefits both players precisely if each originally has \(k=2\), so they are opposite-type interiors. If the exchange is across an edge, that mutual edge remains cross-type and each participant's \(k\in\{0,1\}\) becomes \(1-k\). Both strictly benefit precisely when both vertices were isolated. These are exactly the middle two vertices of a cyclic four-letter alternating factor \(0101\) or \(1010\). Distinct opposite-type interior vertices exist exactly when the cycle contains both a monochromatic \(000\) and a monochromatic \(111\) triple. This proves the necessary-and-sufficient characterization, including the \(n=3\) boundary case.

**Existence.** Relabel types if necessary so \(b\le r\). For \(b=1\), place the unique blue vertex next to a contiguous red run; no blue interior and no adjacent pair of isolated opposite types occurs. If \(b=2k\), use \(k\) blue runs of length two, separated by \(k\) nonempty red runs, possible because \(r\ge b\). All blue vertices are boundary, hence no blue interior or blue isolated vertex exists; the characterization gives stability. If \(b=2k+1\ge3\), create one blue singleton run and \(k\) blue doubleton runs. Separate its singleton from each adjacent blue doubleton by red runs of length at least two; give every other red run positive length. The minimum number of red vertices is \(k+3\). This is at most \(r\) for \(b\ge5\), and for \(b=3\) whenever \(r\ge4\). Again no blue interior exists, and the only blue singleton is not adjacent to a red singleton. The placement is stable. Finally take \(b=r=3\). If each color has one run, there are two opposite interiors. If each has three runs, the cycle alternates and contains \(0101\). If each has two runs, each color has one singleton, and these two singletons are adjacent, again yielding \(0101\). These are all cyclic run structures, proving nonexistence. The latter specific obstruction is the example already in the initiating literature.

**Counting.** A closed walk of length \(n\) in the order-three binary de Bruijn graph corresponds bijectively to a cyclic binary word with \(n\) indexed positions. Each transition incorporates exactly one bit, hence the weight is \(u^{\#\text{blue}}\). Forbidding \(0101\) and \(1010\) is a local transition restriction, while excluding at least one of the two monochromatic triples is the union of two regular languages. Inclusion-exclusion therefore gives the stated coefficient-of-trace formula. It counts rooted, position-labeled circular words, not rotation classes.

**Asymptotics.** Set \(A=M_{\{000\}}(1)\) and \(B=M_{\{000,111\}}(1)\). Color reversal gives identical traces for matrices excluding \(000\) and \(111\). The trace formula summed over all colors, excluding the two monochromatic words, is

\[
S_n=2\operatorname{tr}(A^n)-\operatorname{tr}(B^n)-2.
\]

Exact integer characteristic-polynomial computations yield

\[
\det(tI-A)=t^2(t^6-t^5-2t^3+1),
\]
\[
\det(tI-B)=t^2(t^3-t-1)(t^3+t-1).
\]

The nontransient part of \(A\) is irreducible and contains a self-loop, hence it is primitive; let its Perron root be \(\lambda\). The nonnegative matrix \(B\) is entrywise bounded by \(A\) and has strictly fewer permitted transitions inside that primitive component; Perron–Frobenius strict monotonicity implies \(\rho(B)<\lambda\). Moreover all other eigenvalues of \(A\) have modulus strictly less than \(\lambda\). It follows that \(\operatorname{tr}(A^n)=\lambda^n+o(\lambda^n)\) and \(\operatorname{tr}(B^n)=o(\lambda^n)\). In the primitive component, every row sum is at most two and some are strictly smaller, so irreducibility implies \(\lambda<2\). Branching and a self-loop give \(\lambda>1\). The exact sextic identifies \(\lambda\approx1.651736555\), proving the exponential-rarity statement. These conclusions need no inference from a finite census.

## Verification

The included standalone `verify.py` uses only the Python standard library. It evaluates the original three-level preferences for every opposite-type exchange, separately checks the forbidden-word characterization, and computes weighted transfer traces without using the forbidden-word predicate as its direct oracle. All **65,502** mixed-color, labeled cyclic words for \(3\le n\le15\) were tested, evaluating **3,014,652** candidate opposite-type pairs. All direct and transfer counts matched. Exact Newton-identity arithmetic independently checked the two \(8\times8\) characteristic polynomials. Run `python3 verify.py` to reproduce. The all-size theorem and asymptotic limit are proved above and are not inferred from this finite verification.

## Relationship to prior work

Bilò, Bilò, Lenzner and Molitor (2022), Theorem 2, give the six-vertex equally balanced ring as a nonexistence example when \(\Lambda>1/2\). That special-case obstruction is **not claimed as new**. Their general existence statements and welfare bounds address other parameter regimes and graph classes, and the inspected proof of Theorem 2 does not supply the exact cyclic forbidden-factor criterion, equilibrium enumeration, positive existence for all other cycle splits, or asymptotic density of stable placements. Earlier monotone swap Schelling and vacancy-based jump Schelling models use different deviation/payoff rules, so their stability results cannot directly imply the present classification. A lower-peak cyclic analysis where isolated and boundary players share the same utility similarly does not cover the strict high-peak rank ordering used here.

## Limitations

The theorem is for the stated single-peaked class with \(1/2<\Lambda<1\), exactly two types, no vacancies, ordinary simple cycles, and exchanges that strictly benefit both participants. It does not assert convergence of arbitrary improving paths, welfare bounds, or equilibrium existence on other graphs. Counts are for colorings of labeled positions, not permutations of individually distinguishable agents. Publication-priority uncertainty remains: an unlocated equivalent specialist classification or transfer-matrix result is possible. Self-review is not independent external validation.

## References

1. Davide Bilò, Vittorio Bilò, Pascal Lenzner and Louise Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599, first public version 2022-04-26. https://arxiv.org/abs/2204.12599 ; inspected full text https://arxiv.org/pdf/2204.12599 .
2. Davide Bilò, Vittorio Bilò, Pascal Lenzner and Louise Molitor, *Topological Influence and Locality in Swap Schelling Games*, 2020, arXiv:2005.02752. https://arxiv.org/abs/2005.02752 .
3. *Single-Peaked Jump Schelling Games*, arXiv:2302.12107. https://arxiv.org/abs/2302.12107 .
