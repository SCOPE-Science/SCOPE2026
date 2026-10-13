# Third-order dyadic cancellation in Farhi's integer sequence

## Finding
Let \(a_0=0\) and let \(a_n=\frac n2a_{n-1}+(n-1)!\) for every integer \(n\ge1\). For each integer \(u\ge3\), set
\[
j=2^u,\qquad r=j+u,\qquad N=2^r-j-1.
\]
Then the exact two-adic valuations are
\[
\boxed{\nu_2\left(\sum_{k=1}^{N}\frac{2^k}{k}\right)=2^r-r+3u-2},\qquad
\boxed{\nu_2(a_N)=2^r-2r+3u-1}.
\]
In particular, the truncated logarithm has an excess valuation of exactly \(3u-2\) above the leading order \(2^r-r\), so the excess is unbounded along this explicit family of **non-Mersenne** indices.

## Assumptions and scope
All sums and valuations are taken in the field \(\mathbb Q_2\). The power-series logarithm \(\log(1-z)=-\sum_{k\ge1}z^k/k\) and dilogarithm \(\mathrm{Li}_2(z)=\sum_{k\ge1}z^k/k^2\) converge for \(\nu_2(z)>0\). The claim concerns every integer \(u\ge3\), without primality or extra congruence assumptions; it makes no assertion about indices outside the displayed family. Here \(\nu_2\) is the exponent of \(2\) in a nonzero rational number and \(s_2(n)\) is the binary digit sum.

## Proof
Write \(M=2^r\), \(j=2^u\), and \(B=M-r\). Two identities are needed. First,
\[
\sum_{k\ge1}\frac{2^k}{k}=-\log(1-2)=-\log(-1)=0.
\]
Indeed the \(2\)-adic logarithm is additive on \(1+2\mathbb Z_2\), so twice \(\log(-1)\) is \(\log(1)=0\). Second,
\[
\sum_{k\ge1}\frac{2^k}{k^2}=\mathrm{Li}_2(2)=0.
\]
For completeness, the formal identity
\[
\mathrm{Li}_2(z)+\mathrm{Li}_2\!\left(\frac{z}{z-1}\right)
=-\tfrac12\log^2(1-z)
\]
follows by differentiating both sides and comparing their zero constant terms. It converges in \(\mathbb Q_2\) at \(z=2\); then \(z/(z-1)=2\) and \(\log(-1)=0\), proving the second vanishing identity.

Let \(S_N=\sum_{k=1}^N2^k/k\). By the first vanishing identity, \(-S_N\) is the tail starting with \(k=M-j\). Normalize it by \(2^B\). The contributions from \(k=M-j\) and \(k=M\) add exactly to
\[
\frac{1}{2^j-1}+1=\frac{2^j}{2^j-1},
\]
whose valuation is \(j\). The part \(k>M\) has normalized valuation at least \(r+1\). For \(1\le a<j\), the normalized intermediate contribution is
\[
E=\sum_{a=1}^{j-1}\frac{2^{r-a}}{M-a}.
\]
Replacing each denominator \(M-a\) by \(-a\) changes its summand by
\[
\frac{2^{r-a}M}{a(M-a)},
\]
with valuation \(2r-a-2\nu_2(a)\ge j+3\), because \(a\le j-1\) and \(\nu_2(a)\le u-1\). Thus, modulo elements of valuation at least \(3u-1\),
\[
E\equiv-2^u\sum_{b=1}^{j-1}\frac{2^b}{j-b}
=\sum_{s\ge1}2^{us}H_s,\qquad H_s=\sum_{b=1}^{j-1}\frac{2^b}{b^s}.
\]
The geometric expansion is valid since \(\nu_2(j/b)=u-\nu_2(b)\ge1\). For \(s=1,2\), the two vanishing identities above express \(H_s\) as minus its infinite tail starting at \(b=j\). Every term of that tail has valuation at least \(j-su\); hence \(\nu_2(2^{us}H_s)\ge j\).

For \(s=3\), the unique lowest-valuation term of \(H_3\) is the term \(b=4\), with valuation \(4-3\nu_2(4)=-2\). Indeed for all \(b\ne4\), the value \(b-3\nu_2(b)\) is at least \(-1\). Since \(j\ge8\), this term occurs in \(H_3\); therefore
\[
\nu_2(2^{3u}H_3)=3u-2.
\]
Finally, if \(s\ge4\) and \(b<j\), put \(t=\nu_2(b)\le u-1\). Every summand \(2^{us}2^b/b^s\) has valuation
\[
b+s(u-t)\ge2^t+4(u-t)\ge3u-1.
\]
The last inequality follows from \(u+1+2^t-4t\ge0\) for \(u\ge3\) and \(t\ge0\). Thus all \(s\ge4\) contribute above valuation \(3u-2\). As \(j\ge3u-1\) and \(r+1\ge3u-1\), the omitted endpoint, upper tail, and denominator corrections also contribute above this valuation. Hence
\[
\nu_2(S_N)=B+3u-2=M-r+3u-2.
\]

Unrolling the defining recurrence gives the exact identity \(a_n=(n!/2^n)\sum_{k=1}^n2^k/k\). Legendre's formula yields \(\nu_2(n!/2^n)=-s_2(n)\). Since \(N=(2^r-1)-2^u\) has exactly \(r-1\) ones in binary, \(s_2(N)=r-1\). Therefore \(\nu_2(a_N)=M-r+3u-2-(r-1)=M-2r+3u-1\), completing the proof.

## Verification
The standalone `verify.py` reproduces exact modular-tail valuation computations for \(u=3,4,\ldots,12\) using odd modular inverses; the omitted tail is rigorously above the working precision. Independently, integer arithmetic directly replays the recurrence through \(N=2039\) for \(u=3\), obtaining \(\nu_2(a_{2039})=2034\). Run with `python3 verify.py` in the folder containing this file. These finite computations are checks, not substitutes for the all-\(u\) proof.

## Relationship to prior work
Farhi's April 2022 preprint investigated this integer sequence via Genocchi numbers and its truncated-logarithm representation; the equivalent factorial-convolution sequence was recorded much earlier (OEIS A003149, with an index shift). Dubickas's subsequent study (2024 journal publication) proved the general sharp lower bound \(\nu_2(\sum_{k=1}^n2^k/k)\ge n+1-\log_2(n+1)\), with equality exactly at Mersenne indices. The present family deliberately uses non-Mersenne indices and establishes a growing **excess** via cancellation of logarithmic and dilogarithmic layers followed by the unique cubic layer. Farhi's December 2022 work on \(p\)-adic valuation inequalities and his separate dilogarithmic work provide related tools and context, not this exact sparse-index formula. This is a statement-and-implication comparison; no priority is claimed beyond the actually inspected materials.

## Limitations
The result determines valuations only on the specified sparse infinite family and does not classify all indices of the sequence. The two \(2\)-adic vanishing identities are classical consequences of logarithmic and dilogarithmic functional equations; novelty lies, if not previously recorded, in the third-order cancellation and resulting exact integer-sequence valuation. Equivalents outside the inspected literature may exist. No independent audit or external proof certification has been performed.

## References
1. B. Farhi, *On a curious integer sequence*, arXiv:2204.10136v1 (21 April 2022), especially Proposition 2.2 and Section 3.
2. A. Dubickas, *On a sequence of rational numbers with unusual divisibility by a power of 2*, Miskolc Mathematical Notes 25 (2024), 203–208, DOI:10.18514/MMN.2024.4276, especially Theorem 1 and Section 2.
3. B. Farhi, *Nontrivial lower bounds for the p-adic valuations of some type of rational numbers*, arXiv:2212.00446v1 (1 December 2022), especially Theorems 2.1–2.2.
4. B. Farhi, *Nontrivial lower bounds for the p-adic valuations of some type of rational numbers and an application for establishing the integrality of some rational sequences*, arXiv:2212.03727v1 (7 December 2022), especially the dilogarithm functional equation.
5. OEIS, A003149, factorial-convolution sequence (corresponding to the present sequence shifted by one index); tabulated entries and listed identities do not state the sparse-index valuation theorem.
