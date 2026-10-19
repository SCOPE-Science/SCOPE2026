# A sharp two-threshold renewal-tail law for centered holes in gap shifts

## Finding

Let \(S\subseteq\mathbb N_0\) be any infinite set, and let \(X_S\) be the two-sided binary \(S\)-gap shift. Put \(s_*:=\min S\). For any integers \(a,b>s_*\), forbid the centered word \(0^{a}1 0^{b}\) to obtain \(Y_{a,b}\subseteq X_S\). Write
\[
F(z)=\sum_{s\in S}z^{s+1},\qquad B_k(z)=\sum_{\substack{s\in S\\s\ge k}}z^{s+1}\quad(0<z<1),
\]
and let \(r\in(0,1)\) be the unique solution of \(F(r)=1\). Define \(r_{a,b}\in(r,1)\) as the unique solution of
\[
\boxed{\big(F(r_{a,b})-1\big)\big(1+B_{\max\{a,b\}}(r_{a,b})\big)
=B_a(r_{a,b})B_b(r_{a,b}).}
\]
Then the **exact entropy** and its **sharp moving-hole loss** are
\[
 h(X_S)=-\log r,\qquad h(Y_{a,b})=-\log r_{a,b},
\]
\[
\boxed{\lim_{\min\{a,b\}\to\infty}
\frac{h(X_S)-h(Y_{a,b})}{B_a(r)B_b(r)}
=\frac1{rF'(r)}.}
\]
The joint limit allows either threshold to grow arbitrarily faster than the other. It requires no mixing, eventual periodicity, or regular gap-density hypothesis on \(S\). The formula is invariant under interchanging \(a\) and \(b\), as required by reversal of the forbidden word.

For \(S=\{2^j:j\in\mathbb N_0\}\), write \(D_n=h(X_S)-h(Y_{n,n})\). For every integer \(j\ge1\), the entropies are **exactly constant** for integer \(2^{j-1}<n\le2^j\); when the next power enters the short-gap class,
\[
\boxed{\frac{D_{2^j+1}}{D_{2^j}}\sim r^{2^{j+1}}\longrightarrow0.}
\]
Thus the symmetric centered-hole losses exhibit a sharp lacunary staircase that is not captured by a uniform single-exponential approximation in the word length.

## Assumptions and scope

The shift \(X_S\) is the closure of all bi-infinite concatenations of the blocks \(10^s\), with \(s\in S\); its usual zero-tail limit configurations are included. All entropies are natural-logarithm topological entropies per binary coordinate. Each of \(a,b\) is a positive integer strictly greater than \(s_*\), ensuring short and long gap types are present. The forbidden word \(0^a1 0^b\) is consequently allowed in the unperturbed shift. We use the standard convention that \(\mathbb N_0\) contains zero. The original publication date of the motivating paper is June 25, 2025.

The cutoff quantities \(B_k(r)\) are strictly positive. Since \(S\) is infinite, \(F(0^+)=0\) and \(F(1^-)=\infty\), which guarantees a unique \(r\in(0,1)\); its derivative \(F'(r)=\sum_{s\in S}(s+1)r^s\) is finite and positive.

## Proof

**1. Exactly which gap pairs are forbidden.** If three successive occurrences of the symbol \(1\) have zero-gaps \(s,t\in S\), the middle \(1\) lies in an occurrence of \(0^a1 0^b\) precisely if \(s\ge a\) and \(t\ge b\). Consequently the allowed gap sequences have the single adjacent-pair restriction \(\neg(s\ge a\ \mathrm{and}\ t\ge b)\). This equivalence holds regardless of how sparse \(S\) is. Reversal interchanges the thresholds.

**2. Exact weighted renewal matrix.** Track whether the preceding gap was at least \(a\). With \(U=B_a(z)\), \(V=B_b(z)\), \(W=B_{\max\{a,b\}}(z)\), and \(m=\min\{a,b\}\), the legal weighted gap-transition matrix, in the state order preceding-gap-short / preceding-gap-long, is
\[
M(z)=\begin{pmatrix}
F(z)-U&U\\
F(z)-B_m(z)&U-W
\end{pmatrix}.
\]
The entry in row one, column one sums all gaps below \(a\); the other entries impose the appropriate next-gap bound if the preceding gap was long. Direct expansion in the two possible threshold orders gives the identity
\[
\boxed{\det(I-M(z))=(1-F(z))(1+W)+UV.}
\]
Both the set of gaps below \(m\) and the unbounded set of gaps above \(\max\{a,b\}\) are nonempty. Hence \(M(z)\) is irreducible for every \(z\in(0,1)\), with positive off-diagonal entries; its Perron root is continuous and strictly increasing from zero to infinity. Its determinant is strictly negative, so the non-Perron eigenvalue is negative. At \(z=r\), \(\det(I-M(r))=B_a(r)B_b(r)>0\), which shows that the Perron root is less than one. There is therefore exactly one \(r_{a,b}\in(r,1)\) with Perron root one, and it satisfies the displayed scalar equation.

**3. Transfer radius is binary topological entropy.** Let \(C_N\) be the number of length-\(N\) legal binary words that begin and end with \(1\) and contain at least two ones. Every sequence of finitely many allowed gaps can be extended to a bi-infinite admissible sequence by placing a fixed short gap \(s_*<\min\{a,b\}\) on both sides; hence all such anchored words are genuinely in the language of \(Y_{a,b}\). Their generating series, written \(H(z)=\sum_{N\ge0}C_Nz^N\), is
\[
H(z)=z\,e_0^{\mathsf T}\left(\sum_{j\ge1}M(z)^j\right)\mathbf 1
\]
with \(e_0=(1,0)^{\mathsf T}\) and \(\mathbf 1=(1,1)^{\mathsf T}\). The series converges for positive \(z<1\) exactly when \(\rho(M(z))<1\); its terms are nonnegative and the positive starting state reaches the Perron class.

Writing \(L_N=|\mathcal L_N(Y_{a,b})|\) and \(L(z)=\sum_{N\ge0}L_Nz^N\), each word with at least two ones has a unique first-to-last-one anchored core and at most two boundary zero strings. Words with fewer than two ones number at most \(N+1\). Coefficientwise, for \(0<z<1\),
\[
H(z)\le L(z)\le\frac{1+H(z)}{(1-z)^2}.
\]
The inequalities intentionally overcount potentially forbidden boundary padding in the upper bound; they do **not** assert that all such padding is legal. They show the word-growth generating series and the anchored-gap series have the same radius \(r_{a,b}<1\). Since the radius of \(L\) equals \(e^{-h(Y_{a,b})}\), the claimed entropy formula follows. The same one-state renewal argument (with series \(F\)) establishes \(h(X_S)=-\log r\).

**4. The sharp two-threshold asymptotic.** Put \(\Delta_{a,b}(z)=(1-F(z))(1+B_{\max\{a,b\}}(z))+B_a(z)B_b(z)\). Its unique relevant zero is \(r_{a,b}\), whereas \(\Delta_{a,b}(r)=B_a(r)B_b(r)\). For every \(R<1\), as \(\min\{a,b\}\to\infty\), all three tails \(B_a,B_b,B_{\max}\) and their first derivatives converge uniformly to zero on \([0,R]\). Thus \(\Delta_{a,b}\to1-F\) in \(C^1\) near \(r\). The unique zero tends to \(r\), and the mean-value theorem yields
\[
 r_{a,b}-r=\frac{B_a(r)B_b(r)}{F'(r)}(1+o(1)).
\]
Taking \(\log(r_{a,b}/r)\) proves the displayed limit. The error term holds jointly, without a relation between the rates of increase of \(a\) and \(b\).

**5. Sparse-gap staircase.** For \(S=\{2^j\}\), the short/long partition at threshold \(n\) is constant over each integer interval \(2^{j-1}<n\le2^j\), proving exact entropy plateaus. Moreover, at the jump, \(B_{2^j}(r)\sim r^{2^j+1}\) and \(B_{2^j+1}(r)\sim r^{2^{j+1}+1}\). Applying the already proved two-threshold asymptotic with \(a=b\) on either side yields the stated ratio.

## Verification

Execute `python verify_entropy.py` from the folder containing that accompanying standalone file. It uses the Python standard library only. The actual run passed 20 exact rational renewal/determinant identities; 18 independent finite-state versus scalar-root spectral comparisons, including asymmetric forbidden words; and 7 high-precision lacunary-tail tests. This finite computation is a diagnostic, not a proof of the universal theorem. The infinite proof is the renewal-matrix argument above. The package contains no external or unpublished scientific dependencies.

As a familiar test, \(S=\mathbb N_0\) gives \(r=1/2\). For the symmetric thresholds \(a=b=n\), the theorem predicts \(h(X_S)-h(Y_{n,n})\sim 2^{-(2n+1)}\); this is a consistency test within a well-studied finite-type case, not an independent novelty claim.

## Relationship to prior work

Cheriyath's 2025 paper explicitly leaves the words that both begin and end with zero outside its general gap-shift perturbation theorem, apart from a special arithmetic-gap case. The present theorem treats the natural one-marker subfamily \(0^a1 0^b\), for all infinite gap sets and all asymmetric thresholds. The original paper's complementary endpoint theorem does not imply its joint two-cutoff asymptotic.

Dillon's broader entropy theorem for \(\mathcal S\)-graph shifts already supplies a general generating-matrix framework for length-colored renewal shifts. Via such a recoding, that theorem provides a route to the **fixed-threshold scalar entropy equation**; that equation alone is not claimed to be independent of Dillon's work. The contribution asserted here is the precise, uniform two-moving-threshold **product-of-tails** law, its coefficient for arbitrary infinite \(S\), and its exact sparse staircase implication. These limiting statements are not stated in Dillon's general fixed-graph entropy theorem.

Haydarov, Kadyrov, Makhmudov and Mamayusupov (2026) provide qualitative strict entropy gaps for avoidance of positive-measure cylinders in \(S\)-gap shifts. Their estimate does not give this exact pressure equation or the sharp two-threshold coefficient. Ramirez and Somers (2025) generalize gap shifts with a fixed ambient separating word and give an entropy formula for those systems, rather than a joint rare-word perturbation asymptotic on the binary \(S\)-gap shift.

## Limitations

Only one-marker centered forbidden words are treated; longer centered words containing multiple ones can impose memory of more than one gap and are not classified here. The theorem does not provide a uniform **additive** asymptotic error depending solely on \(a+b\) across all infinite \(S\); the error is relative to the exact two-tail product at fixed \(S\). Classical graph-entropy theory supports the scalar transfer framework, and an equivalent moving-hole asymptotic elsewhere in the broad symbolic-dynamics literature cannot be excluded without further independent bibliographic review. No independent external audit has been performed.

## References

1. Haritha Cheriyath, *A note on the perturbations of subshifts*, arXiv:2506.20750v1 (first public June 25, 2025), Introduction and Section 4. https://arxiv.org/html/2506.20750v1
2. Travis Dillon, *Dynamics and entropy of \(\mathcal S\)-graph shifts*, arXiv:2010.06031 (2020), Theorem 1.2 and Section 4. https://travisadillon.com/documents/S-graph-shifts.pdf
3. Farhod Haydarov, Shirali Kadyrov, Mirmukhsin Makhmudov, Khudoyor Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, arXiv:2606.17031 (2026), Section 7. https://arxiv.org/abs/2606.17031
4. Cristian Ramirez and Amy Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438 (2025), Theorem 1.1. https://arxiv.org/html/2501.08438v1
