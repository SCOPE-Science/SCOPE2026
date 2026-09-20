# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the circuit, PCP, rectangle, and asymptotic-conversion levels.

The balanced counter uses the Boolean identity
\[
\operatorname{carry}(a,b,c)=(a\wedge b)\oplus(c\wedge(a\oplus b)),
\]
whose two product terms are disjoint. Summing the balanced-tree gate count gives exactly \(4m-2k-4\) AND gates per block. The stated fixed-threshold comparator recurrence was exhaustively checked on its Boolean state transitions; two comparisons and the final block combination give the claimed \(4m+2k+1\) per-block bound. Including the cross-block combination gives fewer than \(5km\) gates for every \(k\ge12\), so padding to exactly \(d=5km\) is legitimate.

The source PCP proof is generic for ordered XOR/AND/NOT circuits once every AND output is represented in the certificate: between multiplication gates, all wires are affine in the original input and prior multiplication outputs. The smaller circuit therefore preserves the arithmetization and certificate-uniqueness induction. The original field remains sufficient because \(5k2^k<2^{4k}\), and its polynomial-test soundness remains below \(1/6\).

The source rectangle proof depends on the Gap-Hamming block structure and uniqueness of a valid certificate, not on the original dynamic program. Substituting the new \(d\) therefore leaves the bound \(2^{-m/(8k)}\) unchanged. Substitution into the source input-length formula gives \(N_k=40k^2m^2-3km\), and the explicit constant 51 follows from \(8\sqrt{40}<51\) and \(k\le\log_2N_k\).

The accompanying finite checks confirm the component truth tables and the parameter inequalities for representative values of \(k\). These checks support but do not replace the symbolic proof.

## Originality

The motivating Wang--Wu preprint, submitted on 17 September 2026, explicitly uses an exact-prefix-weight dynamic program with \(d=k(m(m+3)+1)=\Theta(km^2)\) AND gates and states the resulting rectangle upper bound only as \(2^{-n^{\Omega(1)}}\) after translating to total input length. Its detailed construction leaves the Boolean promise circuit modular except for the ordered-AND interface used by the fully linear PCP.

Searches by the paper title and arXiv identifier, by combinations of “Gap-Hamming”, “monochromatic rectangle”, “linear-size circuit”, “AND gates”, “fully linear PCP”, “cheat sheet”, and “square-root”, and by the equivalent quantitative lower-bound formulations did not locate a prior statement of this circuit substitution or the resulting \(2^{-\Omega(\sqrt N/\log^2N)}\) rectangle bound. The current SCOPE archive was also checked by the same mathematical object and claim family, with no overlapping accepted record found.

The novelty claim deliberately excludes the qualitative Wang--Wu separation, the fully linear PCP machinery, and the standard balanced-adder/comparator circuit facts. It is limited to the quantitative strengthening obtained by inserting the linear-AND Gap-Hamming promise circuit into that construction and propagating the improved parameterization through the rectangle and communication-complexity bounds.

Originality is to the best of our knowledge. The motivating paper is extremely recent, creating a material risk of a near-simultaneous observation or an author revision not yet indexed. No inaccessible paper was identified as a specific likely source of prior coverage; the residual risk is primarily recency rather than known-but-unread evidence.

## Value

The change removes an entire factor of \(m\) from the certificate-driving circuit size. In the same construction this changes the total input scaling from \(\Theta(k^2m^3)\) to \(\Theta(k^2m^2)\), converting the source's \(m\)-scale rectangle exponent into an explicit near-square-root exponent in the actual communication input length. It correspondingly strengthens the quantitative lower bounds for \(P^{NP^{cc}}\) and \(P^{RP^{cc}}\) while preserving the polylogarithmic randomized protocol.

## Limitations

The result does not establish optimality of the exponent, a matching rectangle lower bound, or a stronger randomized upper bound. It applies to the Wang--Wu construction and proof template. The finite verification artifact is a sanity check rather than a formal proof.

**Same-model review: passed. Independent audit: not yet performed.**
