# The Bouderbala--Karras divisor discrepancy has infinite global amplitude

## Finding
For a fixed integer \(k\ge1\), define
\[
f_k(1)=0,
\qquad
f_k(n)=\sum_{p^\alpha\parallel n}\gcd(k,\alpha)
\quad(n>1),
\]
and let \(\tau(n)\) denote the number of positive divisors of \(n\). Put
\[
\Delta_k(n)=f_k(n)-\log_2\tau(n).
\]
Then
\[
\sup_{n\ge2}|\Delta_k(n)|=+\infty
\]
for every fixed \(k\ge1\).

The signed range is sharper. If \(k=1\), then
\[
\sup_{n\ge2}\Delta_1(n)=0,
\qquad
\inf_{n\ge2}\Delta_1(n)=-\infty,
\]
and \(\Delta_1(n)=0\) exactly for squarefree \(n\). If \(k\ge2\), then
\[
\sup_{n\ge2}\Delta_k(n)=+\infty,
\qquad
\inf_{n\ge2}\Delta_k(n)=-\infty.
\]

## Assumptions and scope
Write
\[
n=\prod_{i=1}^r p_i^{\alpha_i}
\]
with distinct primes \(p_i\) and positive exponents \(\alpha_i\). The standard divisor formula gives
\[
\log_2\tau(n)=\sum_{i=1}^r\log_2(\alpha_i+1),
\]
and therefore
\[
\Delta_k(n)
=
\sum_{i=1}^r
\left(
\gcd(k,\alpha_i)-\log_2(\alpha_i+1)
\right).
\]
The result concerns the global range as \(n\) varies with \(k\) fixed. It does not assert an asymptotic formula for the extremal discrepancy restricted to \(n\le x\).

## Proof
For \(k=1\), one has \(f_1(n)=\omega(n)=r\), so
\[
\Delta_1(n)
=
\sum_{i=1}^r
\left(
1-\log_2(\alpha_i+1)
\right).
\]
Each summand is nonpositive because \(\alpha_i\ge1\), and it vanishes exactly when \(\alpha_i=1\). Hence
\[
\Delta_1(n)\le0,
\]
with equality exactly when every exponent is \(1\), equivalently when \(n\) is squarefree. On prime powers \(n=q^a\),
\[
\Delta_1(q^a)=1-\log_2(a+1)\longrightarrow-\infty,
\]
which proves the complete \(k=1\) statement.

Now fix \(k\ge2\), and let \(r\) be any prime divisor of \(k\). For distinct primes \(q_1,\ldots,q_t\), set
\[
N_t=\prod_{j=1}^t q_j^r.
\]
Because \(r\mid k\),
\[
\Delta_k(N_t)
=
t\left(r-\log_2(r+1)\right).
\]
For every integer \(r\ge2\),
\[
2^r>r+1,
\]
so \(r-\log_2(r+1)>0\). Therefore
\[
\Delta_k(N_t)\longrightarrow+\infty
\]
as \(t\to\infty\).

For the negative direction, fix a prime \(q\) and set
\[
M_t=q^{kt+1}.
\]
Since \(\gcd(k,kt+1)=1\),
\[
\Delta_k(M_t)
=
1-\log_2(kt+2)
\longrightarrow-\infty.
\]
Thus for every fixed \(k\ge2\) the discrepancy is unbounded in both signs, and in particular its global absolute amplitude is infinite.

## Verification
The proof is symbolic and contains no finite cutoff. The accompanying checker independently evaluates the exponent-sum formula on all exponent tuples of lengths \(1\) through \(4\) with entries from \(1\) through \(10\), verifies the full \(k=1\) sign/equality classification on those tuples, and checks the two explicit positive and negative witness families for every \(2\le k\le40\) and \(1\le t\le30\). These computations are regression checks only; they are not used to justify the infinite statements.

## Relationship to prior work
Bouderbala and Karras introduced the additive function
\[
f_k(n)=\sum_{p^\alpha\parallel n}\gcd(k,\alpha)
\]
and proved the pointwise bounds
\[
\omega(n)\le f_k(n)\le\Omega(n).
\]
In their conclusion they compare these bounds with
\[
\omega(n)\le\log_2\tau(n)\le\Omega(n)
\]
and explicitly leave the amplitude of the difference between \(f_k(n)\) and \(\log_2\tau(n)\) for later consideration. The present result resolves the natural global-over-\(n\) boundedness interpretation of that question and additionally determines the signed global behavior.

Targeted searches for the exact difference, the defining gcd-exponent sum, the absolute-amplitude formulation, and equivalent signed-range statements did not reveal a result implying this classification. The closest retrieved records concerned unrelated gcd maps, discrepancy problems, or other arithmetic functions.

## Limitations
The word “amplitude” in the motivating paper is informal. This result fixes one precise interpretation: the supremum of the absolute discrepancy over all integers \(n\ge2\) for fixed \(k\). It does not determine finer extremal functions such as
\[
\max_{2\le n\le x}|\Delta_k(n)|,
\]
their rates of growth, distributional behavior, or the complete zero set when \(k\ge2\). Literature search cannot by itself prove novelty; an unindexed or differently phrased result remains a residual risk.

## References
M. Bouderbala and M. Karras, “On a new additive arithmetic function related to a fixed integer,” Notes on Number Theory and Discrete Mathematics 28(3) (2022), 575–580. DOI: 10.7546/nntdm.2022.28.3.575-580. Online First: 2022-09-27.
