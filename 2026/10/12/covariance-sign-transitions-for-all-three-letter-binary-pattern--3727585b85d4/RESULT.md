# Covariance sign transitions for all three-letter binary pattern waiting times

## Finding
Let \(B_1,B_2,\ldots\) be independent coin tosses with \(\Pr(B_i=H)=p\) and \(\Pr(B_i=T)=1-p\), where \(0<p<1\). For a three-letter word \(w\), let \(T_w\) be the index of the last toss in the first occurrence of \(w\), allowing overlaps. For distinct words \(a,b\), put \(C_{a,b}(p)=\operatorname{Cov}(T_a,T_b)\).

**Theorem (complete sign classification).** Among the \(\binom{8}{2}=28\) unordered pairs of distinct three-letter words, exactly seven have \(C_{a,b}(p)>0\) for every \(0<p<1\), three have \(C_{a,b}(p)<0\) throughout, fourteen have exactly one sign-changing zero in \((0,1)\), and four have exactly two sign-changing zeros. There are no further interior zeros; every zero is simple.

The following table is complete up to interchanging \(H\) and \(T\). For each representative pair the covariance has the sign of the displayed polynomial in \(p\). The column headed "initial" gives its sign for sufficiently small positive \(p\); every listed interior zero is simple, so the sign alternates across successive zeros. All omitted pairs are obtained by replacing both words by their complements and \(p\) by \(1-p\).

| Words | Sign polynomial | Interior zeros | Initial sign |
| --- | --- | ---: | :---: |
| HHH, HHT | \(-p^4-2p^3-3p^2+2p+1\) | 1 | + |
| HHH, HTH | \(p^4-2p^3-4p^2-2p+2\) | 1 | + |
| HHH, HTT | \(-p^3-3p^2-4p+1\) | 1 | + |
| HHH, THH | \(-5p^4-2p^3-2p^2+2p+1\) | 1 | + |
| HHH, THT | \(p^3-2p-5\) | 0 | - |
| HHH, TTH | \(p^4-3p^3-6p^2-2p+1\) | 1 | + |
| HHH, TTT | \(-p^4+2p^3-2p^2+p-12\) | 0 | - |
| HHT, HTH | \(p^5-4p^4+5p^3+3p^2-6p+2\) | 0 | + |
| HHT, HTT | \(-p^3+6p^2-5p+1\) | 2 | + |
| HHT, THH | \(p^7-3p^5+3p^4+5p^3-6p^2+1\) | 0 | + |
| HHT, THT | \(-5p^3+7p^2+3p-4\) | 1 | - |
| HHT, TTH | \(p^4-2p^3+6p^2-5p+1\) | 2 | + |
| HTH, HTT | \(p^3-2p^2-4p+1\) | 1 | + |
| HTH, THH | \(2p^5-6p^4+6p^3+3p^2-6p+2\) | 0 | + |
| HTH, THT | \(p^6-3p^5+p^4+3p^3-p^2-p+1\) | 0 | + |
| HTT, THH | \(-p^4+2p^3+4p^2-5p+1\) | 2 | + |

In particular, the paired first occurrence times of HHT and HTT have the exact covariance
\[
C_{\mathrm{HHT},\mathrm{HTT}}(p)=
\frac{-p^3+6p^2-5p+1}{p^2(1-p)^2(p^2-p+1)}.
\]
Their covariance is positive for \(0<p<0.3079785283699\ldots\), negative between \(0.3079785283699\ldots\) and \(0.6431041321078\ldots\), and positive above the second threshold. The two constants are exactly the two roots in \((0,1)\) of \(-p^3+6p^2-5p+1=0\).

## Assumptions and scope
Every toss is independent, with the same success probability \(p\), and the alphabet is exactly \(\{H,T\}\). Every stopping time counts the ending position of the first contiguous three-toss match, not the number of matches in a fixed horizon. The two patterns are distinct but can overlap in the underlying sequence; stopping times are taken on the **same** infinite toss sequence. Since \(0<p<1\), all waiting-time moments used here are finite. Endpoint values \(p=0\) and \(p=1\) are excluded. The classification concerns covariance, not independence or the probability that one word wins a pattern race.

## Proof
Fix distinct words \(a,b\). Let \(S\) consist of the empty word and all proper prefixes of \(a\) and \(b\). On reading the next toss, retain the longest suffix belonging to \(S\), unless the new suffix equals \(a\) or \(b\), in which case the race ends. Let \(Q\) be the transient transition matrix and let \(r_a,r_b\) be the one-step absorption columns. All entries belong to \(\mathbb Q(p)\). Every target word occurs eventually with geometric-tail domination, so \(I-Q\) is invertible for \(0<p<1\). Put \(N=(I-Q)^{-1}\), with the row corresponding to the empty word denoted by subscript \(0\).

Let \(\tau=\min(T_a,T_b)\). Standard first-step equations give the following exact column vectors:
\[
 m=N\mathbf1=\mathbb E[\tau\mid\text{state}],\qquad
 s=(2N-I)m=\mathbb E[\tau^2\mid\text{state}],
\]
\[
 w_a=Nr_a=\Pr(T_a<T_b\mid\text{state}),\quad
 w_b=Nr_b,\quad
 h_a=Nw_a=\mathbb E[\tau\mathbf1_{T_a<T_b}\mid\text{state}],\quad
 h_b=Nw_b.
\]
The equal-time event is impossible because the two patterns have the same length and are distinct.

Let \(u_{b\mid a}\) be the expected *additional* tosses needed to see \(b\), starting immediately after \(a\) wins, with the last two tosses of \(a\) retained as initial suffix information. It is computed by the corresponding one-pattern proper-prefix transition matrix: if \(R_b\) is its transient matrix, then \((I-R_b)^{-1}\mathbf1\), evaluated at the longest suffix of \(a\) that is a proper prefix of \(b\), equals \(u_{b\mid a}\). Define \(u_{a\mid b}\) analogously. The future tosses are independent of the past given which word won. Therefore
\[
\begin{aligned}
\mathbb ET_a&=m_0+(w_b)_0 u_{a\mid b},\\
\mathbb ET_b&=m_0+(w_a)_0 u_{b\mid a},\\
\mathbb E(T_aT_b)&=s_0+(h_a)_0u_{b\mid a}+(h_b)_0u_{a\mid b}.
\end{aligned}
\]
Subtracting the product of the first two expressions from the third determines \(C_{a,b}(p)\) exactly as a rational function. This finite-state identity, rather than an asymptotic approximation, proves the reduction for all admissible \(p\).

Eliminating the rational matrices for the sixteen complement-orbit representatives yields the sign-polynomial table. Exact rational-function identities and an independent augmented-state Markov-reward derivation are checked in `verify.py`. The rational-function denominators, after their signs are normalized, consist of products of \(p\), \(1-p\), \(2-p\), \(1+p-p^2\), \(1-p+p^3\), \(p^2-p+1\), and \(1-2r-r^2\) with \(r=p(1-p)\). These factors are positive in \((0,1)\); in particular \(r\le1/4\) gives \(1-2r-r^2\ge7/16\). The displayed sign polynomials differ from the normalized covariance numerators only by factors strictly positive on \((0,1)\).

For each of the sixteen sign polynomials, the exact Sturm root count on \((0,1)\), together with the nonvanishing endpoint values and coprimality with its derivative, gives respectively the zero counts displayed in the table and proves all roots simple. The initial sign is obtained by evaluation near \(p=0\), equivalently by the constant term. Complementing all tosses maps the law at \(p\) to that at \(1-p\); thus these sixteen representatives cover all twenty-eight pairs. Counting complement orbits gives the claimed \(7,3,14,4\) split.

## Verification
Run `python verify.py` with the dependencies in `requirements.txt`. It recomputes all sixteen rational covariances symbolically by the first-winner method, compares each to an independent joint Markov-reward recurrence with separate flags for whether each pattern has appeared, verifies the sixteen denominator factorizations and exact Sturm root counts, checks all twenty-eight pairs at three rational values of \(p\), and confirms the highlighted cubic. The expected output begins `VERIFY_OK` and reports sixteen symbolic cross-checks, eighty-four rational cross-checks, and sixteen Sturm certificates. All operations are exact symbolic or rational arithmetic. Numerical decimals are illustrative approximations only.

## Relationship to prior work
Aki and Hirano (2008) prove a general joint probability-generating-function construction for waiting times of two patterns in Markov-dependent trials; their Theorem 1 and computational recipe provide stronger **distributional machinery** than the first-step identities used here. Their inspected article does not give the complete bias-dependent sign/zero classification for the twenty-eight three-letter binary pairs. In particular, we make no novelty claim for a general joint waiting-time distribution, the finite-state method, or the ability to differentiate a known generating function to recover a covariance. The contribution assessed here is the complete **qualitative covariance phase diagram** with exact root counts and double sign transitions.

Fu and Chang (2002) and Koutras and Milienos (2012) provide broader pattern waiting-time distributional methods; the latter is focused on single-pattern first- and later-occurrence tails. Chen and Zame (1979) treat pattern-order paradoxes for fair coin games. None of the inspected material explicitly supplies the sixteen sign-polynomial root classifications. General joint-PGF formulas make the specialization derivable in principle, so historical priority for the table is not certified.

## Limitations
The phase diagram is specific to two-symbol iid trials and three-letter patterns. It does not classify biased Markov coins, larger alphabets, four-letter patterns, all covariances at once for arbitrary word lengths, or correlations at the degenerate endpoints. The accessible generating-function literature could contain implicit equivalent tabulations; a complete historical-priority conclusion is not established.

## References
- S. Aki and K. Hirano, "Joint Distributions of Waiting Time Random Variables for Patterns," *Journal of the Japan Statistical Society* **38** (2008), 97–105. DOI: 10.14490/jjss.38.97. Public article record: 2008-07-16; free full text inspected at https://www.jstage.jst.go.jp/article/jjss/38/1/38_1_97/_pdf/-char/en.
- J. C. Fu and Y.-M. Chang, "On probability generating functions for waiting time distributions of compound patterns in a sequence of multistate trials," *Journal of Applied Probability* **39** (2002). DOI and pagination not asserted here.
- M. V. Koutras and F. S. Milienos, "Exact and asymptotic results for pattern waiting times," *Journal of Statistical Planning and Inference* **142** (2012), 1464–1479. DOI: 10.1016/j.jspi.2011.12.028.
- R. W. Chen and A. Zame, "On fair coin-tossing games," *Journal of Multivariate Analysis* **9** (1979), 150–156.
