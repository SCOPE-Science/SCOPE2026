# Sharp two-adic valuations of Mersenne-index Domb numbers

## Finding
For every integer \(r\ge3\), the Domb number at the all-ones binary index \(2^r-1\) has exact valuation
\[
\boxed{\nu_2(D_{2^r-1})=3r.}
\]
Equivalently, \(D_{2^r-1}/2^{3r}\) is an odd integer. The proof identifies a unique least-valuation term in a classical alternative Domb sum. The boundary is sharp: \(\nu_2(D_1)=2\) and \(\nu_2(D_3)=8\), whereas the formula is valid from \(r=3\) onward.

## Assumptions and scope
For every integer \(n\ge0\), define the Domb number by
\[
D_n=\sum_{k=0}^{n}\binom nk^2\binom{2k}{k}\binom{2(n-k)}{n-k}.
\]
All binomial coefficients use their usual nonnegative integral arguments; \(\nu_2(m)\) is the exponent of \(2\) in a positive integer \(m\); and \(s_2(m)\) is the number of ones in the standard base-two expansion of \(m\). The theorem is an infinite family of exact statements for \(r\ge3\), not a statement about all indices. Domb numbers also enumerate closed diamond-lattice polygons and form a classical sporadic Apéry-like sequence.

## Proof
Rogers's hypergeometric transformation, Theorem 3.1 and Equation (3.4) of [1], gives the formal-power-series identity
\[
\sum_{n\ge0}D_nz^n=(1-4z)^{-1}
\sum_{k\ge0}\binom{2k}{k}^{\!2}\binom{3k}{k}
\left(\frac{z^2}{(1-4z)^3}\right)^k.
\]
Here the hypergeometric coefficients follow by expanding the indicated \({}_3F_2\) series in [1]. Extracting coefficients of \(z^n\) yields the exact, finite, nonnegative-integer sum
\[
D_n=\sum_{k=0}^{\lfloor n/2\rfloor}P_{n,k},\quad
P_{n,k}=4^{n-2k}\binom{2k}{k}^{\!2}\binom{3k}{k}\binom{n+k}{3k}.
\tag{1}
\]

Legendre's binary-digit formula for factorial valuations gives
\[
\nu_2\binom ab=s_2(b)+s_2(a-b)-s_2(a).
\]
Applying it to each of the three binomial factors in (1), and using \(s_2(2k)=s_2(k)\), gives for every \(0\le k\le\lfloor n/2\rfloor\)
\[
\nu_2(P_{n,k})=2(n-2k)+4s_2(k)+s_2(n-2k)-s_2(n+k).
\tag{2}
\]
In particular, the \(s_2(3k)\) terms from the last two binomial factors cancel exactly.

Fix \(r\ge3\), put \(n=2^r-1\), and reindex by \(k=2^{r-1}-1-j\), so \(0\le j\le2^{r-1}-1\). If \(0\le j\le2^{r-1}-2\), then \(k>0\) and
\[
n-2k=2j+1,\quad s_2(k)=r-1-s_2(j),\quad
s_2(n-2k)=1+s_2(j),\quad
s_2(n+k)=r-s_2(j+1).
\]
The last equality comes from subtracting \(j+1\) from the \((r-1)\)-bit all-ones word and appending a leading one. Substitution into (2) yields the **exact summand-valuation law**
\[
\nu_2(P_{n,\,2^{r-1}-1-j})=3r+4j-1-3s_2(j)+s_2(j+1).
\tag{3}
\]
At \(j=0\), the right-hand side is \(3r\). At every \(1\le j\le2^{r-1}-2\), use \(s_2(j)\le j\) and \(s_2(j+1)\ge1\) to obtain
\[
\nu_2(P_{n,\,2^{r-1}-1-j})-3r
\ge j-1+s_2(j+1)\ge1.
\]
The remaining endpoint \(j=2^{r-1}-1\) corresponds to \(k=0\), and then \(P_{n,0}=4^n\) has valuation \(2n=2^{r+1}-2>3r\). Therefore **exactly one** summand of (1) has valuation \(3r\), with every other summand divisible by \(2^{3r+1}\). Dividing the sum by \(2^{3r}\) leaves one odd integer plus even integers. This proves the result for every \(r\ge3\), without extrapolating from computations.

## Verification
The standalone `verify.py` uses independent exact integer formulas to compare the defining Domb sum with the Rogers-expanded sum for all \(0\le n<80\), checks the proposed valuations for the Mersenne indices \(2^r-1\) with \(1\le r\le9\), and checks 2,044 individual Rogers summands at \(3\le r\le11\) against both valuation identities and the unique-minimum condition. It prints `VERIFY_OK`. These finite tests only corroborate the algebra; Equations (1)–(3) and the inequalities are the proof for all \(r\ge3\).

## Relationship to prior work
Rogers [1] establishes the transformed generating function (used, not claimed as new). Chan and Zudilin [2] supply another Domb representation. Malik and Straub [3] establish Lucas congruences and observe eventual divisibility by four; their result does not fix the unbounded exact exponent at Mersenne indices. Beluhov [4] proves the general lattice-walk lower bound and an equality criterion: in the Domb case this yields a weaker lower bound at binary all-ones indices, not the exact value here. The OEIS Domb entry [5] records definitions, alternative sums, and a short value table, but no stated Mersenne valuation law. Supercongruences for shifted generalized Domb sums concern different objects or index families and do not imply (3).

## Limitations
The theorem does not classify \(\nu_2(D_n)\) at arbitrary \(n\), the odd factor modulo higher powers of two, or valuations at odd primes. The transformed summation formula is prior work. The comparison with literature and mathematical databases does not rule out an unindexed equivalent theorem; independent originality assessment has not been performed.

## References
[1] M. D. Rogers, *New 5F4 hypergeometric transformations, three-variable Mahler measures, and formulas for 1/pi*, arXiv:0704.2438, first publicly posted 2007-04-18, Theorem 3.1, Equation (3.4). https://arxiv.org/abs/0704.2438

[2] H. H. Chan and W. Zudilin, *New representations for Apéry-like sequences*, Mathematika 56 (2010). https://mrc.sdu.edu.cn/ziliao/60.pdf

[3] A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297, 2015, Sections 3 and 5. https://arxiv.org/abs/1508.00297

[4] N. Beluhov, *Powers of 2 in High-Dimensional Lattice Walks*, arXiv:2506.12789, 2025, Theorem and Section 7. https://arxiv.org/abs/2506.12789

[5] OEIS Foundation, A002895, *Domb numbers*, definitions, formulas, and references. https://oeis.org/A002895
