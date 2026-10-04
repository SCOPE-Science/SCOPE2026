# Positive \(\mu\)-Sondow small-witness conjecture reduces to new Fermat primes

## Finding
For an integer \(\mu\), a positive integer \(n\) is \(\mu\)-Sondow when every prime \(p\mid n\) satisfies
\[
p^{\nu_p(n)}\mid \frac{n}{p}+\mu.
\]
Let \(S_\mu\) denote the set of such integers.

For every positive integer
\[
\mu\notin\{1,2,4,16\},
\]
if
\[
S_\mu\cap[2,\mu]=\varnothing,
\]
then
\[
\mu=2^{2^s}
\]
and the Fermat number
\[
F_s=2^{2^s}+1
\]
is prime for some \(s\ge5\).

Equivalently, the positive half of Conjecture 1(i) in Grau--Oller-Marcén--Sadornil is proved for every parameter except, potentially, powers of two immediately preceding a presently unknown Fermat prime. In particular, any positive counterexample would imply the existence of a Fermat prime beyond \(F_4\).

The two nonexcluded parameters arising from the known Fermat primes are not counterexamples:
\[
145\in S_{256},\qquad 627\in S_{65536}.
\]

## Assumptions and scope
The source conjecture states that, apart from the seven exceptional integer parameters listed there, every \(\mu\) should have a nontrivial \(\mu\)-Sondow number not exceeding \(|\mu|\). This note treats only positive \(\mu\), so the excluded positive parameters are \(1,2,4,16\).

The primary source first appeared publicly as arXiv:2111.14211v1 on 28 November 2021. The result here does not address negative \(\mu\), nor does it prove that a new Fermat-prime parameter would actually be a counterexample; it proves only the one-way implication from a positive counterexample to a new Fermat prime.

## Proof
Suppose first that \(\mu\ge3\) is odd. Take \(n=2\). The only prime divisor is \(2\), and
\[
\frac{n}{2}+\mu=1+\mu
\]
is even. Thus \(2\in S_\mu\), and \(2\le\mu\).

Now suppose that \(\mu\) is even but is not a power of two. Write
\[
\mu=2^v m,
\]
where \(v=\nu_2(\mu)\ge1\) and \(m\ge3\) is odd. Set
\[
n=2^{v+1}.
\]
Then
\[
\frac{n}{2}+\mu=2^v(1+m),
\]
which is divisible by \(2^{v+1}=n\), because \(m+1\) is even. Hence \(n\in S_\mu\). Also
\[
n=2^{v+1}\le2^v m=\mu.
\]
So every even non-power of two has a witness in the required interval.

It remains to consider
\[
\mu=2^v.
\]
If \(\mu+1\) is composite, let \(p\) be any prime divisor of \(\mu+1\) and take \(n=p\). Then
\[
\frac{n}{p}+\mu=1+\mu
\]
is divisible by \(p\), so \(p\in S_\mu\). Because \(p\) is a proper divisor of the composite integer \(\mu+1\),
\[
2\le p\le\mu.
\]
Thus a positive counterexample can occur only if \(\mu=2^v\) and \(2^v+1\) is prime.

The classical factorization argument now forces \(v\) itself to be a power of two. Indeed, write
\[
v=2^s t
\]
with \(t\) odd. If \(t>1\), then with \(x=2^{2^s}\),
\[
2^v+1=x^t+1
\]
is divisible by \(x+1\), contradicting primality. Hence \(t=1\), so
\[
v=2^s,
\]
and \(2^v+1=F_s\) is a Fermat prime.

For \(s=0,1,2\), the parameters are \(2,4,16\), which are explicitly excluded by the source conjecture. For \(s=3\), the parameter is \(\mu=256\). The integer
\[
145=5\cdot29
\]
is \(256\)-Sondow because
\[
29+256=285=5\cdot57
\]
and
\[
5+256=261=29\cdot9.
\]
Thus \(145\in S_{256}\) and \(145\le256\).

For \(s=4\), the parameter is \(\mu=65536\). The integer
\[
627=3\cdot11\cdot19
\]
is \(65536\)-Sondow because
\[
209+65536=65745=3\cdot21915,
\]
\[
57+65536=65593=11\cdot5963,
\]
and
\[
33+65536=65569=19\cdot3451.
\]
Thus \(627\in S_{65536}\) and \(627\le65536\).

Therefore any positive counterexample not among the source's explicit exceptions must correspond to a Fermat prime \(F_s\) with \(s\ge5\), proving the claim.

## Verification
The accompanying `verify.py` checks the two exceptional Fermat-prime witnesses \(145\in S_{256}\) and \(627\in S_{65536}\) directly from the definition. It also regression-tests the constructive witnesses for positive parameters through \(50000\), whenever the relevant case is not a Fermat-prime shell.

The infinite reduction is proved symbolically above; the finite computation is not used as a substitute for that proof.

## Relationship to prior work
Grau, Oller-Marcén, and Sadornil introduce \(\mu\)-Sondow numbers, give several equivalent formulations, and pose Conjecture 1(i), which asks for a nontrivial member of \(S_\mu\) at most \(|\mu|\) for every parameter outside a short exceptional list. Their paper provides constructions and computational evidence but does not state the Fermat-prime reduction above.

Targeted searches using the paper title, the conjecture label, the phrases “power of two” and “Fermat prime,” the parameters \(256\) and \(65536\), and the equivalent small-witness formulation did not locate a prior statement of this reduction. Semantic literature searches likewise returned no covering result.

## Limitations
The reduction is one-way: a new Fermat prime would merely identify another parameter not covered by the elementary constructions above; it would not imply failure of the \(\mu\)-Sondow conjecture.

The result says nothing about negative parameters. Literature non-detection also cannot exclude an unindexed note or observation containing the same elementary reduction.

## References
1. J. M. Grau, A. M. Oller-Marcén, and D. Sadornil, “On \(\mu\)-Sondow numbers,” arXiv:2111.14211v1, first posted 28 November 2021.
2. J. M. Grau, A. M. Oller-Marcén, and D. Sadornil, “On \(\mu\)-Sondow numbers,” *Acta Mathematica Hungarica* 168 (2022), 217--227, DOI 10.1007/s10474-022-01271-w.
