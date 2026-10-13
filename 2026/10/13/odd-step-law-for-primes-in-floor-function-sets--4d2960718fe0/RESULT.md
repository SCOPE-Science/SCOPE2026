# Odd step law for primes in floor-function sets
## Finding
For every odd integer \(N\ge 5\), define
\[
\mathcal S(N)=\left\{\left\lfloor\frac{N}{k}\right\rfloor:1\le k\le N\right\},
\qquad
G(N)=\#\bigl(\mathcal S(N)\cap\mathbb P\bigr).
\]
Let \(P^+(N)\) denote the largest prime factor of \(N\). Then
\[
G(N)-G(N-1)=
\begin{cases}
1,&P^+(N)\ge\sqrt N,\\
0,&P^+(N)<\sqrt N.
\end{cases}
\]
Consequently, if \(N=p_1p_2p_3\) with distinct odd primes \(2<p_1<p_2<p_3\), then
\[
G(N)=G(N-1)+1\quad\Longleftrightarrow\quad p_3>p_1p_2,
\]
and otherwise \(G(N)=G(N-1)\). This proves Conjecture 4 of Heyman's 2021 preprint.

## Assumptions and scope
The theorem concerns integer arguments \(N\ge5\) that are odd. The exceptional odd integer \(N=3\) is intentionally excluded: the prime \(3\) enters the floor set while \(2\) leaves, so \(G(3)-G(2)=0\). No primality, squarefreeness, or fixed number of prime factors is assumed in the general theorem.

For a prime \(p\), put
\[
D_p(N)=\left\lfloor\frac{N}{p}\right\rfloor-
\left\lfloor\frac{N}{p+1}\right\rfloor.
\]
This is the number of integers \(k\) satisfying \(N/(p+1)<k\le N/p\), hence \(p\in\mathcal S(N)\) exactly when \(D_p(N)>0\).

## Proof
First observe the exact one-step identity
\[
D_p(N)-D_p(N-1)=\mathbf 1_{p\mid N}-\mathbf 1_{p+1\mid N}.
\]
Indeed, \(\lfloor N/m\rfloor-\lfloor(N-1)/m\rfloor\) is \(1\) precisely when \(m\mid N\), and is otherwise \(0\).

Next suppose \(p\le\sqrt{N-1}\), and set \(t=\lfloor(N-1)/p\rfloor\). Then \(t\ge p\), while \(N-1<p(t+1)\le t(p+1)\). Hence
\[
\left\lfloor\frac{N-1}{p+1}\right\rfloor\le t-1<
\left\lfloor\frac{N-1}{p}\right\rfloor,
\]
so \(D_p(N-1)>0\). The same argument at \(N\) shows \(D_p(N)>0\). Thus every prime at or below \(\sqrt{N-1}\) occurs in both floor sets and contributes no change to \(G\).

For \(p\ge\sqrt N\), the interval \(N/(p+1)<k\le N/p\) has length
\[
\frac{N}{p(p+1)}<1,
\]
so \(D_p(N)\in\{0,1\}\), and likewise \(D_p(N-1)\in\{0,1\}\). If \(N\) is not a square there is no integer, hence no prime, strictly between \(\sqrt{N-1}\) and \(\sqrt N\). If \(N\) is a square, the only possible boundary prime is \(p=\sqrt N\), which is already covered by this interval-length argument.

Now \(N\ge5\) is odd, so every prime \(p\ge\sqrt N\) is odd. Therefore \(p+1\) is even and cannot divide \(N\). The one-step identity reduces to
\[
D_p(N)-D_p(N-1)=\mathbf 1_{p\mid N}
\qquad(p\ge\sqrt N).
\]
Because both sides \(D_p(N)\) and \(D_p(N-1)\) are zero or one in this range, such a prime enters \(\mathcal S(N)\) exactly when it divides \(N\), and no prime in this range leaves. At most one prime divisor of \(N\) can be at least \(\sqrt N\). Summing the prime indicators proves the displayed step law.

For \(N=p_1p_2p_3\) with distinct odd primes, \(N\) is not a square and its largest prime factor is \(p_3\). The inequality \(p_3>\sqrt N\) is equivalent to \(p_3>p_1p_2\). This is exactly the dichotomy in Heyman's Conjecture 4.

## Verification
A standard-library checker independently evaluates \(G(N)\) from the distinct floor quotients and compares it with the largest-prime-factor criterion for every odd \(5\le N\le100000\). It also exhaustively checks every triple of distinct odd primes with product at most \(100000\). The checker reports

`VERIFY_OK odd_n=49998 triple_cases=10618 max_n=100000`

These finite checks are regression tests only. The theorem is established by the symbolic argument above and does not depend on the cutoff.

## Relationship to prior work
Heyman introduced this exact prime-counting problem for floor-function sets, proved \(G(p)=G(p-1)+1\) for primes \(p\ne3\), proved the analogous statement for products of two odd primes, and stated the three-distinct-prime dichotomy above as Conjecture 4 after a limited computation. The present theorem proves that conjecture and explains it as one instance of a general odd-integer step law.

Ma and Wu later sharpened the asymptotic prime-counting theorem for the same floor-function set and used the same exact indicator
\(
\mathbf 1(\lfloor N/p\rfloor-\lfloor N/(p+1)\rfloor>0)
\), but their result is asymptotic in \(N\) and does not give the exact one-step law above. Their paper classifies the subject under primary MSC 11N37.

The current MathDB page for the three-prime formula still records the statement as open. The current OEIS entry A067514 gives the underlying sequence, a floor-factorial reformulation, and asymptotics, but no criterion for odd one-step increments in terms of \(P^+(N)\).

## Limitations
The theorem is deliberately restricted to odd \(N\). For even \(N\), a large prime \(p\) may leave because \(p+1\mid N\), so the parity argument that rules out losses no longer applies. The proof does not provide a comparable closed formula for every even step. The originality comparison cannot exclude an obscure unpublished or unindexed proof, although the focal paper, the later full-text follow-up, current database records, and targeted searches were checked.

## References
1. Randell Heyman, “Primes in floor function sets,” arXiv:2111.00408, first submitted 31 October 2021; later published in INTEGERS 22 (2022), A59.
2. Rong Ma and Jie Wu, “On the primes in floor function sets,” arXiv:2112.12426; Bulletin of the Australian Mathematical Society 108 (2023), 236–243, DOI 10.1017/S0004972722001277.
3. OEIS A067514, the sequence counting distinct primes of the form \(\lfloor n/k\rfloor\) for \(1\le k\le n\).
4. MathDB problem 352434, “The three-prime floor-function set formula.”
