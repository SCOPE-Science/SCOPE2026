# Odd-divisor omission rigidity for binary–prime-power near-perfect numbers

## Finding
For all integers \(k\ge 1\) and \(e\ge 2\), let \(p\) be an odd prime and set
\[
n=2^k p^e, \qquad \mathcal D_{\rm odd}(n)=\{1,p,p^2,\ldots,p^e\}.
\]
For **every** subset \(T\subseteq\mathcal D_{\rm odd}(n)\), the following equivalence holds:
\[
\boxed{\sigma(n)=2n+\sum_{d\in T}d}
\quad\Longleftrightarrow\quad
\boxed{p=2^{k+1}-1\ \text{ and }\ T=\{p,p^2,\ldots,p^{e-1}\}}.
\]
In particular, the all-odd omission set is unique whenever it exists, and then has precisely \(e-1\) distinct members. For every fixed Mersenne prime \(p=2^{k+1}-1\), varying \(e\) gives examples with arbitrarily many required odd omitted divisors. This is an infinite-exponent statement, not an assertion that infinitely many Mersenne primes exist.

## Assumptions and scope
Here \(\sigma\) denotes the sum of all positive divisors. A set of \(s\) **distinct** positive divisors \(T\) is an omission set when \(\sigma(n)-2n=\sum_{d\in T}d\), equivalently when the sum of the proper positive divisors outside \(T\) is \(n\). In the displayed characterization, every omitted divisor is automatically proper because \(p^{e-1}<2^kp^e\). We impose the natural parity restriction that **all** omitted divisors are odd. We do not assert uniqueness among arbitrary deletion sets that contain even divisors. The prime is odd; the exponents satisfy \(k\ge1\) and \(e\ge2\). The claim covers every such parameter, with no size cutoff.

## Proof
Write \(M=2^{k+1}-1\) and \(Q=\sum_{j=0}^{e-1}p^j\). The divisor sum factors as
\[
\sigma(n)=M\sum_{j=0}^{e}p^j=M(Q+p^e),\qquad 2n=(M+1)p^e.
\]
Since \(p^e=(p-1)Q+1\), subtraction gives the exact identity
\[
\sigma(n)-2n=MQ-p^e=(2^{k+1}-p)Q-1.
\tag{1}
\]
Suppose some \(T\subseteq\{1,p,\ldots,p^e\}\) satisfies the omission equation. Equation (1) becomes
\[
(2^{k+1}-p)Q=1+\sum_{d\in T}d.
\tag{2}
\]
Index the selected divisors by a set \(J\subseteq\{0,1,\ldots,e\}\), meaning \(T=\{p^j:j\in J\}\). We have \(p^e\equiv1\pmod Q\). Set
\[
r=|J\cap\{0,e\}|\in\{0,1,2\},\qquad
R=1+r+\sum_{\substack{j\in J\\1\le j\le e-1}}p^j.
\]
The right side of (2) is congruent to \(R\pmod Q\); thus \(Q\mid R\). Moreover,
\[
1\le R\le 3+\sum_{j=1}^{e-1}p^j=Q+2<2Q,
\]
because \(Q\ge1+p\ge4\). The only multiple of \(Q\) in this interval is \(Q\), hence \(R=Q\). Taking this equation modulo \(p\) yields \(1+r\equiv1\pmod p\), since \(Q\equiv1\pmod p\). With \(0\le r\le2<p\), necessarily \(r=0\). We consequently have
\[
\sum_{\substack{j\in J\\1\le j\le e-1}}p^j
=Q-1=\sum_{j=1}^{e-1}p^j.
\]
Every summand is positive, so all internal exponents occur and no endpoints occur: \(J=\{1,2,\ldots,e-1\}\). Therefore
\[
T=\{p,p^2,\ldots,p^{e-1}\},\qquad 1+\sum_{d\in T}d=Q.
\]
Substituting into (2) and cancelling \(Q>0\), we obtain \(2^{k+1}-p=1\), or \(p=2^{k+1}-1\). This proves the necessity and uniqueness.

Conversely, if \(p=2^{k+1}-1\) is prime and \(T=\{p,p^2,\ldots,p^{e-1}\}\), equation (1) simplifies to
\[
\sigma(2^kp^e)-2\cdot2^kp^e
=Q-1=\sum_{j=1}^{e-1}p^j=\sum_{d\in T}d.
\]
All members of \(T\) are distinct odd proper divisors. The converse and the cardinality assertion follow. \(\square\)

## Verification
The exact identity, modular reduction, interval \(Q\le R<2Q\), and the prime-modulus bound \(0\le r\le2<p\) supply the infinite proof. A separate exhaustive exact-arithmetic check in `verify.py` enumerates **every subset** of the odd divisors for \(1\le k\le10\), odd primes \(3\le p\le97\), and \(2\le e\le8\). It checks \(1{,}680\) parameter triples and \(243{,}840\) candidate subsets and finds precisely \(21\) matching cases (seven exponents each for the Mersenne primes \(3,7,31\) appearing in this range), with exactly the predicted unique subset in each matching case. The finite check is corroboration, not the proof for unrestricted exponents.

For example, with \(k=1\), \(p=3\), and \(e=4\), we have \(n=162\), \(\sigma(n)=363\), and \(\sigma(n)-2n=39=3+9+27\); no other all-odd omission subset exists.

To reproduce, execute `python3 verify.py` using an ordinary Python 3 interpreter; the program has no external dependencies.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery, and Zelinsky, *On 2-Near Perfect Numbers* (first public arXiv version, 2 October 2023; journal publication in 2024), establish two-omission classifications when the odd prime exponent is one or two. Their object motivates studying controlled omitted divisors of \(2^kp^e\). Fearon, Foushee, Porosoff, Skula, Zelinsky, and Zhang, *Complete characterization of 2-near perfect numbers with exactly 2 prime factors* (arXiv:2508.06651v3, 2026), prove that for odd-prime exponent at least three **exactly two omitted divisors** are possible only when the exponent is three and the omitted set is \(\{p,p^2\}\) for a Mersenne prime. The present statement instead classifies **every all-odd omission set of any cardinality**, including the previously untreated exponents \(e\ge4\) with \(e-1\ge3\) odd deletions. This includes the known low-exponent Mersenne examples as boundaries, not as new claims.

The known general results on near-perfect numbers and the cited two-omission classifications do not directly determine these higher-cardinality all-odd sets. Unrestricted deletion sets, in which even divisors are permitted, remain outside the conclusion. A 2016 thesis by Adajar on near-perfect numbers with \(k\) divisors is listed in the later paper's references but was not available in full for comparison; an equivalent statement there or in unindexed literature remains a possible originality risk.

## Limitations
No classification of omission subsets containing even divisors is claimed. The theorem does not determine the unrestricted minimum number of omitted divisors, nor does it require or prove infinitude of Mersenne primes. The hypothesis that the odd prime exponent is at least two is essential to the argument as written; the one-exponent problem is not addressed. The related literature comparison is limited to the identified and accessible sources; external independent review has not been performed.

## References
1. V. Aryan, D. Madhavani, S. Parikh, I. Slattery, and J. Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305, first submitted 2 October 2023; *Integers* **24** (2024), A61. https://arxiv.org/abs/2310.01305.
2. R. Fearon, H. Foushee, B. Porosoff, A. Skula, J. Zelinsky, and K. Zhang, *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, arXiv:2508.06651v3 (28 September 2026). https://arxiv.org/abs/2508.06651.
3. P. Pollack and V. Shevelev, *On perfect and near-perfect numbers*, *Journal of Number Theory* **132** (2012), 3037–3046, DOI:10.1016/j.jnt.2012.06.008.
4. C. F. E. Adajar, *On near-perfect and deficient-perfect numbers with k divisors*, master's thesis, University of the Philippines Diliman (2016), cited in reference 2; full text not inspected.
