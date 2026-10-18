# Exact mixed-prime ambiguity of ordered periodic-orbit direction signatures

## Finding
Let \(p\ge3\) be an odd prime and let \(S=\{0,1,\ldots,2p-1\}\) with its usual order. For a permutation \(f:S\to S\) consisting of one \(2p\)-cycle, define its complete left-right signature
\[
 L_f(i,t)=\mathbf 1_{\{f^t(i)\le i\}},\qquad i\in S,\quad 0\le t<2p.
\]
Write \(M(n)\) for the maximum number of distinct \(n\)-cycles on an ordered \(n\)-point set with a common complete signature. Then
\[
 \boxed{M(2p)=2^{p-1}\quad\text{for every odd prime }p.}
\]
The upper bound is valid for every signature, not merely for a generic one; the lower bound is attained by an explicit family of \(2^{p-1}\) different cycles.

## Assumptions and scope
The full time-indexed comparison table is supplied, with labels tied to the fixed order. An \(n\)-cycle is a permutation with exactly one orbit of cardinality \(n\). Distinct permutations are counted separately even if they have identical underlying point sets. This is a finite orbit-reconstruction theorem motivated by continuous interval-map periodic dynamics: any prescribed permutation of a finite ordered subset of an interval extends by linear interpolation to a continuous self-map of the interval. No claim is made that members of the constructed family define globally mixing interval maps or have the same full period spectrum as maps of the interval.

## Proof
**Phase-prefix lemma.** Fix an \(n\)-cycle \(f\), write its ordered points \(x_1<\cdots<x_n\), and let \(a_j\in\mathbb Z/n\mathbb Z\) be the unique phase with \(f^{a_j}(x_1)=x_j\). Thus \(a_1=0\). Suppose phases \(a_1,\ldots,a_i\) have been reconstructed, and put \(A_i=\{a_1,\ldots,a_i\}\). For \(1\le t<n\), the signature row of \(x_{i+1}\) obeys
\[
 L_f(i+1,t)=\mathbf 1_{\{a_{i+1}+t\in A_i\}},
\]
where sums are modulo \(n\). At time zero, change the known entry from one to zero, because \(a_{i+1}\notin A_i\). The resulting binary word is exactly a cyclic translate of the indicator of \(A_i\). Given \(A_i\), any admissible phase is therefore in a coset of the translation stabilizer
\[
 H_i=\{h\in\mathbb Z/n\mathbb Z:A_i+h=A_i\}.
\]
If a phase exists, precisely \(|H_i|\) phases match that row: all coset translations are outside \(A_i\), since \(A_i\) is a union of \(H_i\)-cosets. Such choices may be extended or discarded by subsequent rows. The stabilizer order divides both \(n\) and \(|A_i|=i\).

**Upper bound.** Set \(n=2p\). For \(1\le i<2p\), the only possible nontrivial stabilizer orders are \(2\), occurring only at even indices \(i\), and \(p\), occurring only at \(i=p\). There are \(p-1\) even indices before \(2p\). If \(|H_p|=p\), then \(A_p\) is a full orbit under addition by two, and, because \(0\in A_p\), it is exactly the even residue class. No earlier \(A_i\subsetneq A_p\) can have order-two stabilizer: order two means invariance under addition by \(p\), which sends an even residue to an odd residue. Likewise no later \(A_i\supseteq A_p\), with \(i<2p\), has order-two stabilizer: invariance by addition of \(p\) would force inclusion of all odd residues as well. Hence, along **any** admissible reconstruction path, the product of successive numbers of phase choices is at most
\[
 \max\{p,2^{p-1}\}=2^{p-1}.
\]
To turn this pathwise statement into a uniform bound on the number of completions, form the finite rooted tree of consistent partial phase assignments. Give every child of a node equal conditional probability. A full leaf has probability the reciprocal of the product of its branching numbers, hence at least \(2^{-(p-1)}\). The probabilities of all full leaves sum to at most one, even if some partial paths terminate early. Therefore there are at most \(2^{p-1}\) full leaves. Every compatible cycle determines a distinct full leaf, so \(M(2p)\le2^{p-1}\).

**Sharpness.** Divide \(S\) into ordered adjacent two-point blocks \(B_j=\{2j,2j+1\}\) for \(0\le j<p\). Choose freely \(p-1\) bits \(\varepsilon_0,\ldots,\varepsilon_{p-2}\in\{0,1\}\). Define a permutation by
\[
 f(2j+s)=2(j+1)+(s\oplus\varepsilon_j)\quad(0\le j<p-1),
\]
\[
 f(2(p-1)+s)=s\oplus1\oplus\varepsilon_0\oplus\cdots\oplus\varepsilon_{p-2},
\]
where \(s\in\{0,1\}\) and \(\oplus\) means addition modulo two. Each step advances one block cyclically; after precisely \(p\) steps the within-block bit is flipped, so this is a single \(2p\)-cycle. For every \(t\) not divisible by \(p\), the iterate moves to a distinct block and the left/right comparison is determined solely by the starting and ending block indices. For \(t=p\), the iterate flips the bit inside its own block, again determining the comparison independently of the choices. The time-zero row is fixed. Hence all \(2^{p-1}\) permutations have exactly the same complete signature. They are pairwise distinct because the first \(p-1\) block maps reveal the chosen bits. Thus \(M(2p)\ge2^{p-1}\), completing the proof.

## Verification
Run `python3 verify.py` from this package. The self-contained program exhaustively enumerates the \((n-1)!\) single cycles for each \(2\le n\le10\), independently computing each complete signature. In particular it obtains \(M(6)=4\) and \(M(10)=16\), precisely the values predicted for \(p=3\) and \(p=5\). It also constructs the explicit block families for \(n=6,10,14,22\) and checks distinctness, cyclicity, and signature equality. These finite checks are diagnostic; the upper and lower bounds for all odd primes follow from the preceding proof, not enumeration.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi, *Period spectrum and rigidity of interval maps* (arXiv:2610.07435v1, public 5 October 2026), Lemma 2.1, prove uniqueness of the left/right signature for prime cycle lengths, while their Section 2 observes that composite lengths admit nonuniqueness. Their results do not provide an exact maximum multiplicity for the squarefree mixed-prime lengths \(2p\). An earlier quantitative bound for general \(n\) gives \(M(n)\le\prod_{i=1}^{n-1}\gcd(n,i)\), with equality only for prime powers; at \(n=2p\) it yields \(M(2p)\le p2^{p-1}\), rather than the sharp bound here. Previous algorithmic work on the same signatures accelerates reconstruction when the length is prime and does not settle mixed-prime multiplicities. The present parity-exclusion argument removes the extra factor \(p\).

## Limitations
The theorem concerns lengths equal to twice an odd prime. It does not determine \(M(n)\) for arbitrary mixed-prime integers, or the full distribution of signature-class sizes. The constructed permutations are not asserted to be periodic orbits of a single common global interval map, and no rigidity claim for topologically mixing interval maps follows from this construction.

## References
1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (5 October 2026), Sections 1–2 and 5. https://arxiv.org/pdf/2610.07435
2. *Quadratic-time reconstruction of prime cycles from left-right orbit signatures* (2026), archived research statement.
