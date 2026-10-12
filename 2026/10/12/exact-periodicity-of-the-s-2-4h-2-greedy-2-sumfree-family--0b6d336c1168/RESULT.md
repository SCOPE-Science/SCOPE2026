# Exact periodicity of the \(S_{2,4h+2}\) greedy 2-sumfree family

## Finding
For every integer \(h\ge2\), put \(g=4h+2\) and \(M=3g+3\). Let \(S_{2,g}\) be the increasing sequence beginning with \(2,g\), each later term being the least integer larger than the preceding one that is not a sum of **two distinct** earlier selected terms. Define
\[
R_h=\{2+4j:0\le j<h\}\cup\{g+4j,g+4j+1:0\le j\le h\}\cup\{2g+3+4j:0\le j\le h\}\pmod M.
\]
Then the exact infinite sequence is
\[
\boxed{S_{2,g}=\{2,2g+2\}\cup\{g+4j,g+4j+1:0\le j\le h\}\cup\{n\ge2g+3:n\bmod M\in R_h\}.}
\]
The least eventual period in the integer membership indicator is \(M=12h+9\); the least period of consecutive differences is \(g+1=4h+3\), with exactly \(2h+4\) earlier entries. Its natural density is \(1/3\).

## Assumptions and scope
All parameters are integers with \(h\ge2\), \(g=4h+2\). Only sums of **two distinct** terms are forbidden, not doubled single terms. The residue representatives in \(R_h\) lie in \([0,M)\). The claimed periodic tail starts at \(2g+3\), not at the first seed. No claim is made about the other congruence classes of \(g\), or about general initial pair \((f,g)\).

## Proof
**Residue exclusion.** The four arithmetic-progression blocks in \(R_h\), each with step \(4\), are
\[
[2,g-4]_4,\quad[g,2g-2]_4,\quad[g+1,2g-1]_4,\quad[2g+3,3g+1]_4,
\]
where \([a,b]_4=\{a,a+4,\ldots,b\}\). Set \(e=2g+2\). Exact arithmetic-progression sum calculations show
\[
R_h\cap(R_h+R_h)=\varnothing,\qquad R_h\cap(e+R_h)=\varnothing\pmod M.
\]
The finite arithmetic-interval certificate below proves both identities **for every** \(h\ge2\), using a uniform affine-endpoint reduction. Thus no two elements of the proposed periodic residue classes sum into those classes, and adding the exceptional term \(e\) likewise never reaches a periodic class. The only candidate member below \(2g+3\) whose residue is not treated by this modular argument is \(e=2g+2\): below it, the candidate consists of \(2\) and \(g,g+1,g+4,g+5,\ldots,2g-2,2g-1\). A sum with \(2\) is at most \(2g+1\), while the only sum of two distinct terms from the last displayed blocks below \(2g+4\) is \(g+(g+1)=2g+1\). Hence \(e\) is not forbidden. Its self-sum is irrelevant because summands must be distinct. This proves sum exclusion globally.

**Saturation of all omitted integers.** For finite arithmetic progressions with common step \(4\), the sum of two *different* blocks \([a,b]_4\), \([c,d]_4\) is exactly \([a+c,b+d]_4\). For a single block, sums of two **distinct** elements fill exactly \([2a+4,2b-4]_4\), empty if the block is a singleton. The proposed set below \(5M\) consists of the five initial blocks
\[
\{2\},\quad[g,2g-2]_4,\quad[g+1,2g-1]_4,\quad\{2g+2\},\quad[2g+3,3g+1]_4,
\]
followed, for each \(1\le k\le4\), by the four blocks \(kM+R_h\). Applying the preceding exact sum formulas, and separating integers by residue modulo \(4\), gives the exhaustive finite inclusion
\[
[g,5M)\subset S_{2,g}\cup(S_{2,g}\widehat{+}S_{2,g}),
\]
where \(\widehat{+}\) denotes sums of *distinct* members. The executable interval certificate checks the inclusion for every \(2\le h\le132\).

**Why that finite calculation proves every parameter, not merely tested cases.** All these block endpoints, their distinct-pair sum endpoints, the three modular translates needed for residue exclusion, and the window endpoints are affine integral expressions in \(h\) with slopes divisible by \(4\). After restricting to a fixed residue modulo \(4\) and dividing by \(4\), every adjusted endpoint is \(\alpha h+\beta\) for integers \(\alpha,\beta\), with \(-7\le\beta\le23\) (computed directly from the finite endpoint formulas; verified independently by `artifacts/verify_greedy_2_4hplus2.py`). Coverage and disjointness of unions of integer intervals depend only on comparisons between such endpoints and their one-unit successors. Two such comparisons with unequal integral slopes cannot switch order for \(h\ge33\), because their constant terms differ by at most \(31\); with equal slopes their comparison is fixed for all \(h\). Thus checking \(2\le h\le132\), as the script does with exact integers, **proves the two residue identities and the finite inclusion uniformly for all** \(h\ge2\). This is a finite certificate of a parameter-uniform affine-interval argument, not an inference from a long initial segment of any infinite sequence.

For any omitted \(n\ge4M\), write \(n=n_0+kM\) with \(4M\le n_0<5M\) and \(k\ge0\). Tail membership is periodic, so \(n_0\) is also omitted. The finite inclusion supplies distinct selected \(a<b\) with \(n_0=a+b\). As \(n_0\ge4M\), necessarily \(b\ge M\), hence \(b\) is a periodic-class term (the only exceptional selected terms are smaller than \(M\)). Therefore \(b+kM\) remains selected and exceeds \(a\), and \(n=a+(b+kM)\) is forbidden. Together with the finite interval, all omissions are forbidden. Since all proposed members survive, the greedy construction is exactly the claimed set.

**Sharp period and preperiod.** The circular ordered gaps of the residue set \(R_h\) are \(1\), \(3\), and \(4\); each pair \((g+4j,g+4j+1)\) contributes a gap \(1\). Each such gap is followed by \(3\) except the last, which is followed by \(4\). Consequently the consecutive circular gap pattern \((1,4)\) occurs exactly once. Any rotational symmetry of \(R_h\) must fix this unique location, hence is trivial. Thus its minimum additive period is \(M\). As \(|R_h|=h+2(h+1)+(h+1)=4h+3=g+1\), the minimal first-difference period has length \(g+1\). Before the tail, exactly \(2+2(h+1)=2h+4\) members are selected, the last being \(2g+2\not\equiv R_h\pmod M\); its transition to the next member has gap \(1\) instead of the circular residue gap \(4\), so the repeating differences cannot start earlier. Finally \(|R_h|/M=(g+1)/(3g+3)=1/3\).

## Verification
Run `python3 artifacts/verify_greedy_2_4hplus2.py` using standard Python 3. The script performs exact progression sum and modular collision tests, the affine-endpoint bound calculation, and complete coverage by selected terms or two distinct selected summands up to \(5M\) for each \(2\le h\le132\). It also independently generates the greedy sequence for \(2\le h\le13\) and compares all terms below \(5M\), and verifies the unique circular gap pattern. Expected stdout is `artifacts/verification_output.txt`. The extrapolation to all \(h\) follows from the proved affine-comparison lemma; the direct simulations alone are not used as an infinite proof.

## Relationship to prior work
D. van Berkel and W. Bosma propose ultimate periodicity of all strict greedy 2-sumfree sequences in *On \(t\)-sumfree sequences* (arXiv:2609.16843, first posted 15 September 2026) and formulate exact period/preperiod predictions in *Periodicity conjectures for all 2-sumfree sequences* (arXiv:2609.18522, first posted 16 September 2026). Their cited proved general region \(g\le2f\) does not reach \(f=2\), \(g=4h+2\ge10\); finite computational evidence is not a uniform proof. Published analyses establish the full \(f=1\) column and certain families with \(f\ge4\) or \(f\ge5\), which are distinct parameter families and do not imply this \(f=2\) progression. Historical \(s\)-additive work is a residual possible source of an equivalent description. The two original manuscripts could not be read in full through accessible public text routes; the comparison uses their accessible abstracts, quoted theorem/conjecture statements in later published discussions, and the material inspected in those related works.

## Limitations
The result concerns only \(f=2\), \(g\equiv2\pmod4\) with \(g\ge10\). It does not settle all greedy 2-sumfree sequences, does not cover the other \(g\) residue classes, and has not received independent mathematical audit. The method uses an explicitly replayable exact finite certificate plus a proved uniform endpoint-stability reduction; no unchecked computational range is asserted to establish infinite behavior. Potential equivalence with older unindexed \(s\)-additive literature remains an originality risk.

## References
1. D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843v1 (15 September 2026), https://arxiv.org/abs/2609.16843.
2. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1 (16 September 2026), https://arxiv.org/abs/2609.18522.
3. *Complete periodicity of the \(f=1\) greedy strict 2-sumfree family*, published-finding corpus, 18 September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-complete-f1-greedy-2-sumfree-periodicity--056019251c4e.
4. *Exact periodicity of the first two off-diagonal greedy 2-sumfree families*, published-finding corpus, 20 September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-first-two-off-diagonal-2-sumfree-families--dc29809f76be.
5. R. Queneau, *Sur les suites s-additives*, J. Combin. Theory Ser. A 12 (1972), 31–71, DOI:10.1016/0097-3165(72)90083-0 (full text not inspected).
