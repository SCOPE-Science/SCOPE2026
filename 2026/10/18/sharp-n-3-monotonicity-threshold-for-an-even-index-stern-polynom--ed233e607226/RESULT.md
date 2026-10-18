# Sharp \(n=3\) monotonicity threshold for an even-index Stern-polynomial family

## Finding
For every even integer \(k\ge2\), let \(Q_k(t)=B_{53\cdot2^k-3}(t)\), with Stern polynomials defined below. Then
\[
Q_k\text{ is strictly increasing on }\mathbb R\quad\Longleftrightarrow\quad k\in\{2,4,6,8,10,12\}.
\]
For every even \(k\ge14\), an exact negative derivative occurs at the *same* rational point \(t=-13/20\). In particular, the suggested cutoffs \(c_{2i}=3\) for \(7\le i\le16\) in Ulas's Conjecture 4.2(1) cannot be valid. This is **not** a counterexample to the conjecture's eventual-monotonicity clause for each fixed \(k\).

## Assumptions and scope
For all integers \(m\ge1\), the polynomials in \(\mathbb Z[t]\) are defined by
\[
B_0(t)=0,\quad B_1(t)=1,\quad B_{2m}(t)=tB_m(t),\quad B_{2m+1}(t)=B_m(t)+B_{m+1}(t).
\]
Ulas defines \(p_{k,n}=2^{2n+k}-3\cdot2^{n+k-1}+2^k-3\). At \(n=3\), one has \(p_{k,3}=53\cdot2^k-3\); the result concerns **all** even \(k\ge2\) at this single fixed \(n=3\). "Increasing" means nondecreasing; the six positive cases are in fact strictly increasing. No claim is made for odd \(k\) or for other \(n\).

## Proof
**1. Exact decomposition.** The standard Stern identity (Schinzel; also [3, Lemma 2.1]) gives, for every integer \(k\ge2\),
\[
B_{53\cdot2^k-3}(t)=B_{2^k-3}(t)B_{53}(t)+B_3(t)B_{52}(t).
\]
Directly from the recurrence,
\[
B_{2^k-3}(t)=1+2\sum_{j=1}^{k-2}t^j,\quad
B_{53}(t)=1+4t+5t^2+3t^3,
\]
\[
B_{52}(t)=t^2+2t^3+2t^4,\quad B_3(t)=1+t.
\]
Writing \(S_k(t)=1+2\sum_{j=1}^{k-2}t^j\), we consequently obtain the exact finite polynomial identity
\[
Q_k(t)=S_k(t)(1+4t+5t^2+3t^3)+(1+t)(t^2+2t^3+2t^4).
\tag{1}
\]
The empty sum at \(k=2\) is zero. This identity may also be proved directly by induction from the defining recurrence.

**2. The infinite negative-derivative branch.** Suppose \(k\ge14\) is even. Set \(x=-t\),
\[
C(x)=1-4x+5x^2-3x^3,\quad D(x)=x^2-2x^3+2x^4.
\]
The geometric sum in (1) gives
\[
Q_k(-x)=\frac{(1-x+2x^{k-1})C(x)+(1-x^2)D(x)}{1+x}.
\tag{2}
\]
Differentiate (2) over \(\mathbb Q(x)\) and substitute \(x=13/20\); straightforward exact rational simplification yields
\[
\left.\frac{d}{dt}Q_k(t)\right|_{t=-13/20}
=\frac{80(82203k+108923)(13/20)^{k-2}-1026127}{17424000}.
\tag{3}
\]
The positive term \(h_k=(82203k+108923)(13/20)^{k-2}\) strictly decreases along even integers \(k\ge14\): indeed,
\[
\frac{h_{k+2}}{h_k}=\left(\frac{13}{20}\right)^2\frac{82203(k+2)+108923}{82203k+108923}<1
\]
for every \(k\ge14\), as follows by multiplying out the positive denominator. At \(k=14\), equation (3) is exactly
\[
Q'_{14}(-13/20)=-\frac{4258510596084063}{163840000000000000}<0.
\]
Thus (3) is negative for every even \(k\ge14\), so none of these polynomials is increasing on \(\mathbb R\).

**3. The six positive cases.** For \(k=2,4,6,8,10,12\), expand the explicit finite identity (1), differentiate, and execute Euclid's exact rational Sturm algorithm. The resulting signs at the two infinite endpoints have the following variations, in order \(k=2,4,6,8,10,12\):
\[
V(-\infty)=(2,2,3,4,5,6),\qquad V(+\infty)=(2,2,3,4,5,6).
\]
Each \(Q_k'\) therefore has exactly zero distinct real roots. The values \(Q_k'(0)\) are, respectively, \(4,6,6,6,6,6\); hence \(Q_k'(t)>0\) for every real \(t\) in each of the six cases. The exact rational coefficient and Sturm-chain computations are fully specified, reproducible, and independently checked against direct Stern recursion in the bundled `VERIFY.py`. Together with Step 2, these exhaust all even \(k\ge2\). \(\square\)

## Verification
Run `python3 VERIFY.py` using Python's standard library alone. It checks the exact closed expression against the binary Stern recurrence for the six positive cases and further sample indices; constructs univariate exact rational Sturm chains without floating-point arithmetic; checks the six endpoint variation pairs and constant derivative signs; and independently evaluates the rational witness (3) and its monotonicity bound. The execution returns `VERIFY_OK`. Finite recurrence comparisons and sampled values are **not** proofs of the infinite branch; the proof of that branch is the rational formula and monotonicity argument in Step 2. The six Sturm certificates are finite exact exhaustive algebraic checks.

## Relationship to prior work
Ulas [1], Conjecture 4.2(1), proposes eventual strict monotonic behavior in the even-\(k\) family and reports candidate cutoffs \(c_{2i}=3\) up to \(i=16\), apart from a separate \(k=34\) example. The present result shows that the sample cutoff cannot hold for \(i=7,\ldots,16\). It does **not** disprove existence of some later cutoff for those fixed indices. The general Stern identities used in Step 1 appear in [2] and [3]; none of those cited identities asserts the sharp monotonicity threshold or the common rational negative-derivative witness. Earlier work [3] primarily treats polynomial zero regions and irreducibility, not real monotonicity of this later-indexed family. Novelty outside the inspected literature has not been independently certified.

## Limitations
The theorem is restricted to the single slice \(n=3\), even \(k\ge2\), and real monotonicity. It makes no claim about real-root counts, irreducibility, or eventual behavior as \(n\) grows for any fixed \(k\). The derivation of formula (3) and the finite small-\(k\) Sturm computations require exact arithmetic; both are verifiable from the accompanying source. An unindexed equivalent derivation remains a possible prior-work risk.

## References
[1] M. Ulas, *Strong arithmetic property of certain Stern polynomials*, arXiv:1909.10844v1 (24 September 2019), especially Section 2 and Conjecture 4.2(1). https://arxiv.org/abs/1909.10844

[2] M. Ulas and O. Ulas, *On certain arithmetic properties of Stern polynomials*, arXiv:1102.5109 (2011), especially Section 2. https://arxiv.org/abs/1102.5109

[3] K. Dilcher, M. Kidwai and H. Tomkins, *Zeros and irreducibility of Stern polynomials*, Publ. Math. Debrecen 90 (2017), 407–433, especially Section 2, Lemma 2.1. https://doi.org/10.5486/PMD.2017.7620
