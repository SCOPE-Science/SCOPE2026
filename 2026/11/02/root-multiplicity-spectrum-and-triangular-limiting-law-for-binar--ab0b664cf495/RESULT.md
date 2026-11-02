# Root-multiplicity spectrum and triangular limiting law for binary two-one shuffle squares

## Finding

For each integer \(m\ge1\), consider all length-\(2m\) binary words containing exactly two ones. A **shuffle root** of such a word \(W\) is a length-\(m\) binary word \(X\) for which the positions of \(W\) can be partitioned into two increasing subsequences that both read \(X\). Distinct roots are distinct words, not distinct colorings or interleavings. Denote the number of distinct roots by \(R(W)\), and write
\[H_t(m)=\#\{W\in\{0,1\}^{2m}:|W|_1=2,\ R(W)=t\}.\]

Define \(\binom{r}{3}_{+}\) as \(\binom{r}{3}\) for integers \(r\ge3\), and as zero for \(r<3\). **The complete root-multiplicity distribution** is
\[H_0(m)=\binom{m+1}{2}-1,\qquad H_t(m)=\binom{m-3t+5}{3}_{+}-2\binom{m-3t+2}{3}_{+}+\binom{m-3t-1}{3}_{+}\quad(t\ge1).\]
Its positive-root bivariate generating function is
\[\sum_{m\ge1}\sum_{t\ge1}H_t(m)z^m u^t=\frac{uz(1+z+z^2)^2}{(1-z)^2(1-uz^3)}.\]

In a more explicit form, putting \(j=m-3t+2\), one has \(H_t(m)=0\) when \(j<0\), and otherwise
\[H_t(m)=\begin{cases}1,&j=0,\\4,&j=1,\\10,&j=2,\\9(j-1),&j\ge3.\end{cases}\]
Consequently the possible positive root counts are **exactly** \(1,2,\ldots,\lfloor(m+2)/3\rfloor\), and the number of one-root words is \(1,4,10\) at semilengths \(1,2,3\), respectively, then \(9(m-2)\) for every \(m\ge4\).

**Limiting root-count law.** If \(W_m\) is sampled uniformly from the \(\binom{2m}{2}\) two-one words, then the distribution of \(R(W_m)/m\) converges weakly to
\[\frac14\delta_0+\frac92(1-3s)\,\mathbf1_{(0,1/3)}(s)\,ds.\]
In particular, for each fixed \(0<s<1/3\),
\[\lim_{m\to\infty}\Pr\left(\frac{R(W_m)}m\ge s\right)=\frac34(1-3s)^2.\]
Conditional on \(R(W_m)>0\), the limiting density is \(6(1-3s)\) on this interval and the expected number of distinct roots is asymptotic to \(m/9\).

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\); the distinguished symbol \(1\) occurs precisely twice. The length is an even positive integer \(2m\) with \(m\ge1\). There are no restrictions on the positions of the two ones, and the two shuffled copies need not form disjoint *contiguous* factors. The number of different position colorings producing the same root is ignored. All formulas count words, not rotation classes, necklaces, or reversal classes. Only the first content layer with a nonconstant root is considered; no higher-weight classification is asserted.

## Proof

**1. Exact root intervals.** Write each word uniquely as \(W=0^a1\,0^b1\,0^c\), with \(a,b,c\ge0\) and \(a+b+c=2d\), where \(d=m-1\). Each root necessarily has one \(1\), hence is uniquely of the form \(X_x=0^x1\,0^{d-x}\) for some integer \(0\le x\le d\).

We claim that \(X_x\) is a root of \(W\) **if and only if**
\[x\le a\le2x,\qquad d-x\le c\le2(d-x).\tag{1}\]
For necessity, the first \(1\) in \(W\) must belong to one of the two copies. That copy has already used all \(x\) of its initial zeros; the other copy has used between zero and \(x\) initial zeros. Thus \(x\le a\le2x\). By reversing both the word and the two roots, the analogous argument after the second \(1\) gives \(d-x\le c\le2(d-x)\).

For sufficiency, give the copy whose \(1\) is first the initial \(x\) zeros. Give the other copy the remaining \(a-x\) initial zeros. Between the two ones place the remaining \(2x-a\) zeros preceding the second copy's \(1\) and the \(2(d-x)-c\) suffix zeros following the first copy's \(1\). These counts are nonnegative by (1), and their sum is \(b=2d-a-c\). After the second \(1\), assign \(c-(d-x)\) zeros to the first copy and \(d-x\) to the second copy. Every copy then reads \(X_x\), proving sufficiency. Thus all allowed roots correspond to the **consecutive integer interval**
\[\max\!\left(\left\lceil\frac a2\right\rceil,d-c\right)\le x\le\min\!\left(a,d-\left\lceil\frac c2\right\rceil\right).\tag{2}\]
An interval with its lower endpoint above its upper endpoint is empty.

**2. Counting consecutive roots.** For \(t\ge1\), let \(I_t(m)\) count pairs \((W,x)\) such that \(W\) has all of the \(t\) roots \(X_x,X_{x+1},\ldots,X_{x+t-1}\). Requiring (1) at both endpoints gives
\[x+t-1\le a\le2x,\qquad d-x\le c\le2(d-x-t+1).\tag{3}\]
The admissible starting roots satisfy \(t-1\le x\le d-2t+2\). For each such \(x\), there are exactly \((x-t+2)(d-x-2t+3)\) ordered choices \((a,c)\), each uniquely specifying a nonnegative \(b=2d-a-c\). With \(D=d-3t+3=m-3t+2\) and \(y=x-t+1\), this yields
\[I_t(m)=\sum_{y=0}^{D}(y+1)(D-y+1)=\binom{D+3}{3}_{+}=\binom{m-3t+5}{3}_{+},\tag{4}\]
where the sum is empty if \(D<0\). The middle equality is a standard binomial convolution and also follows by expanding the quadratic summand.

A word having \(r\) distinct roots contributes \(\max(r-t+1,0)\) to \(I_t\), because by (2) its root indices form an interval. Taking the second discrete difference therefore extracts words with **exactly** \(t\) roots:
\[H_t(m)=I_t(m)-2I_{t+1}(m)+I_{t+2}(m).\tag{5}\]
Inserting (4) proves the displayed binomial formula. For each fixed \(t\), the length generating function is
\[\sum_{m\ge1}H_t(m)z^m=\frac{z^{3t-2}(1-z^3)^2}{(1-z)^4}=\frac{z^{3t-2}(1+z+z^2)^2}{(1-z)^2}.\tag{6}\]
Summing (6) against \(u^t\) gives the stated bivariate generating function. Expanding \((1+z+z^2)^2/(1-z)^2\) gives coefficients \(1,4,10,18,27,36,\ldots\), namely \(9(j-1)\) for \(j\ge3\), so all allowed positive root counts genuinely occur.

**3. Known total count and the zero-root class.** Summing (5) over all positive \(t\) telescopes to \(I_1(m)-I_2(m)\), giving
\[\#\{W:R(W)>0\}=\binom{m+2}{3}_{+}-\binom{m-1}{3}_{+}=1+\frac{3m(m-1)}2.\tag{7}\]
Equation (7) is the **previously published weight-two shuffle-square total** [1], not a claim of new enumeration. Subtracting it from the \(\binom{2m}{2}\) possible words gives \(H_0(m)=\binom{m+1}{2}-1\).

**4. Scaling limit.** For positive integers \(t\) with \(j=m-3t+2\ge3\), the exact coefficient is \(9(m-3t+1)\). In particular, if \(t/m\to s\) with \(0<s<1/3\), then \(H_t(m)/m\to9(1-3s)\). Since \(\binom{2m}{2}/m^2\to2\), Riemann summation gives the limiting density \(\frac92(1-3s)\) on \((0,1/3)\). The excluded endpoint strips contain at most \(O(m)\) words per fixed number of root levels; there are no other positive values by the exact spectrum. The zero-root mass satisfies \(H_0(m)/\binom{2m}{2}\to1/4\). Thus the weak limit is the asserted atom plus triangular density, whose continuous mass is \(3/4\). Integrating the density over \((s,1/3)\) gives the sharp survival probability. Finally, \(\sum_W R(W)=I_1(m)=\binom{m+2}{3}\), and division by the known positive-root total (7) gives \(\mathbb E[R(W_m)\mid R(W_m)>0]\sim m/9\).

## Verification

A standalone script, `checker.py`, independently decides whether a given word is an interleaving of two copies of a proposed root using a dynamic program on the two consumption positions. For every two-one binary word of semilength \(1\) through \(24\), it compares all possible distinct roots to the interval criterion (2), then compares the complete histogram to (5), checks the known total and the zero-root class. This is exhaustive **for those finite lengths only**. The script checks another 100 semilengths against the generating-function coefficients and incidence identity. Its recorded output is in `checker_output.txt`; run with `python3 checker.py`. The finite computations corroborate the all-length proof but do not replace it.

## Relationship to prior work

Grytczuk, Pawlik and Pleszczyński [1, Theorem 3 and Corollary 1] already classified **which** length-\(2m\), weight-two words are shuffle squares and established the exact total in (7). Both facts are explicitly treated as **prior results**, not new discoveries. Their statement does not give counts split by the number of distinct shuffle roots. Datko and Pawlik [2, Proposition 1] counted how many shuffle squares each one-one root **generates**, and [2, Theorem 2] identified several explicit (one-root) classes; the reverse question of the entire multiplicity distribution and its limit law is not answered there. The exact inverse-root spectrum (5) and the triangular law require controlling overlaps between roots, which the source-to-target count alone does not resolve. The 2025 structural paper [3] treats other shuffle-square restrictions; [4] establishes generic parity-conditioned asymptotics, not root multiplicities in the sparse two-one layer. A recent prior-research index search found no equivalent exact multiplicity law, but absence from an index is not proof of priority.

## Limitations

The theorem concerns precisely two occurrences of one symbol, and ignores multiplicity of interleaving partitions for a given root. Complementation transfers the formula to words with exactly two zeros, but no claim is made for words with four or more ones or for nonbinary alphabets. The total positive count and the resulting approximately three-quarter shuffle-square **existence density** were already implicit in [1]; only the newly split root-multiplicity distribution, generating function, and scaled ambiguity law are advanced as contributions. No exhaustive literature index or independent proof review is asserted.

## References

1. J. Grytczuk, B. Pawlik, and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first posted 2023-08-26), Section 2.4, Theorem 3 and Corollary 1. https://arxiv.org/abs/2308.13882
2. D. Datko and B. Pawlik, *Roots of Binary Shuffle Squares*, Symmetry **17** (2025), article 305, published 2025-02-17, especially Proposition 1, Theorem 2, and Conjecture 1. https://doi.org/10.3390/sym17020305
3. J. Grytczuk, B. Pawlik, and A. Ruciński, *Shuffle squares and nest-free graphs*, arXiv:2503.22043 (first posted 2025-03-27). https://arxiv.org/abs/2503.22043
4. X. He and L. Post, *Asymptotically half of binary words are shuffle squares*, arXiv:2512.12077 (first posted 2025-12-12). https://arxiv.org/abs/2512.12077
5. X. He, E. Huang, I. Nam, and R. Thaper, *Shuffle squares and reverse shuffle squares*, arXiv:2109.12455 (first posted 2021-09-25). https://arxiv.org/abs/2109.12455
