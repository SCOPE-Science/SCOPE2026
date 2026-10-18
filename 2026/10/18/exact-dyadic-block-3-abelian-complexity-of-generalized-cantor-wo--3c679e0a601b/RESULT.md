# Exact dyadic-block 3-Abelian complexity of generalized Cantor words

## Finding

For every integer \(q\ge4\) and every integer \(k\ge1\), let \(c_q\) be the infinite fixed point beginning with \(1\) of
\[\mu_q(1)=10^{q-2}1,\qquad \mu_q(0)=0^q.\]
For a finite binary word \(u\), write \(|u|_v\) for the number of *contiguous* occurrences of \(v\) in \(u\). Two words of equal length are **3-Abelian equivalent** when \(|u|_v=|w|_v\) for every word \(v\) of length at most three. Let \(\mathcal P^{(3)}_{c_q}(n)\) count equivalence classes of length-\(n\) factors of \(c_q\).

**Theorem.** At every substitution-block length \(q^k\),
\[
\boxed{\mathcal P^{(3)}_{c_q}(q^k)=
\begin{cases}
5\cdot2^k-4,&q=4,\\
5\cdot2^k-3,&q\ge5.
\end{cases}}
\]
More precisely, put \(R=2^k\). The complete list of class labels \((K,a,b)\), where \(K\) is the number of ones, \(a\) is the two-letter prefix and \(b\) is the two-letter suffix, consists of \((0,00,00)\), \((R,10,01)\), and, for each \(1\le K<R\), the five pairs
\[
(a,b)\in\{(00,00),(00,01),(00,10),(01,00),(10,00)\},
\]
with exactly one exception: at \(q=4\), \(K=R-1\), the label \((K,00,00)\) does not occur. Distinct listed labels give distinct 3-Abelian classes.

Consequently the 2-Abelian complexity at these lengths is \(3\cdot2^k-1\): the finer 3-Abelian partition splits its mixed-boundary 2-Abelian classes, and the exceptional missing class occurs only when \(q=4\).

## Assumptions and scope

The alphabet is \(\{0,1\}\), factor means contiguous factor, and a 3-Abelian statistic counts overlapping occurrences. The positive integer \(k\) denotes substitution depth, not the order of Abelian equivalence. The theorem concerns factors of the **infinite** fixed point, at lengths exactly \(q^k\), with \(q\ge4\). It makes no statement about the ordinary Cantor word \(q=3\) or lengths between substitution powers. Prefixes and suffixes of length two are well defined since \(q^k\ge4\).

## Proof

**1. Complete factor-language reduction.** Put \(L=q^k\) and \(W=\mu_q^k(1)\). By induction, \(W\) is a palindrome, begins and ends in \(1\), has length \(L\), and contains \(R=2^k\) ones. Distinct ones in \(W\) are separated by at least \(q-2\ge2\) zeros: each newly formed nonzero letter is an endpoint of a block \(10^{q-2}1\), while images of intervening symbols preserve or enlarge the zero runs.

Because \(\mu_q^k(0)=0^L\), decomposing \(c_q\) into successive aligned length-\(L\) blocks produces blocks \(W\) and \(0^L\). The positions of nonzero blocks reproduce the original fixed point, which itself separates successive ones by at least two zeros. Thus any length-\(L\) interval meets at most one nonzero block. The complete factor set is therefore
\[
\mathcal F_{c_q}(L)=\{0^L,W\}\cup
\{0^{L-t}W[0:t],\;W[L-t:L]0^{L-t}:1\le t<L\}.
\]
Here \(W[0:t]\) is the first \(t\) symbols and \(W[L-t:L]\) the last \(t\). Conversely all these factors occur at the two ends of the explicit block \(\mu_q^{k+1}(1)=W0^{(q-2)L}W\); the interior gap has at least \(2L\) zeros. This establishes equality, including endpoint cases.

**2. Reconstruction of the 3-Abelian signature.** Every factor avoids \(11\) and \(101\), since successive ones are at distance at least three. Let \(u\) have length \(L\), contain \(K\) ones, and have first two symbols \(u_0,u_1\) and last two \(u_{L-2},u_{L-1}\). The only possible length-three factors other than \(000\) are \(001\), \(010\), and \(100\), with counts
\[
\begin{aligned}
|u|_{001}&=K-u_0-u_1,\\
|u|_{010}&=K-u_0-u_{L-1},\\
|u|_{100}&=K-u_{L-2}-u_{L-1},\\
|u|_{000}&=L-2-|u|_{001}-|u|_{010}-|u|_{100}.
\end{aligned}
\]
Indeed, each nonboundary one has two zeros immediately preceding it, two zeros immediately following it, and two zero neighbors, except exactly where the relevant two- or one-symbol boundary prevents a three-letter factor. The length-two counts also follow from these length-three counts and the final two symbols (count all length-three occurrences ending in or starting with a specified two-letter pattern). Hence \((K,u[0:2],u[L-2:L])\) determines every count through length three.

Conversely, counts through length three determine \(K\), and determine the two-letter prefix and suffix: for any binary two-letter word \(v\),
\[
\mathbf1_{\{\text{prefix}_2(u)=v\}}
=|u|_v-\sum_{a\in\{0,1\}}|u|_{av},\qquad
\mathbf1_{\{\text{suffix}_2(u)=v\}}
=|u|_v-\sum_{a\in\{0,1\}}|u|_{va}.
\]
Thus two factors are 3-Abelian equivalent **if and only if** their labels \((K,a,b)\) agree.

**3. Exhaustive label classification.** The factor \(0^L\) supplies \((0,00,00)\); the only factor with \(R\) ones is \(W\), supplying \((R,10,01)\). Fix \(1\le K<R\), and let \(p_K\) be the zero-based position of the \(K\)-th one in \(W\). A left-zero-padded prefix of \(W\) ending immediately at that one (cut \(t=p_K+1\)) has label \((K,00,01)\). Ending one position later (\(t=p_K+2\)) gives \((K,00,10)\), since the remaining left padding has length at least two: the next one lies at least three positions away. Both prefixes exist for every specified \(K\).

Ending two positions later (\(t=p_K+3\)) gives a suffix \(00\). For \(K\le R-2\), there remain at least two left padding zeros and the label is \((K,00,00)\). For \(K=R-1\), the trailing gap in \(W\) equals \(q-2\), so the left padding has exactly \(q-3\) zeros. If \(q\ge5\), there are at least two, again giving \((K,00,00)\); if \(q=4\), there is one and the label instead equals \((K,01,00)\). Since \(W\) is a palindrome, reversing these factors produces \((K,01,00)\) from \((K,00,10)\), and \((K,10,00)\) from \((K,00,01)\). Thus all claimed labels exist, except possibly \((R-1,00,00)\) at \(q=4\).

No additional labels are possible: the complete factor list in Step 1 says each nontrivial mixed factor is a zero-padded prefix or a zero-padded suffix of \(W\). Its zero-padded end has two initial/final zeros unless the padding has length one, in which case its two-letter boundary is \(01\) or \(10\). The other boundary belongs to \(\{00,01,10\}\), and these possibilities give only the five listed labels. For the excluded case, any mixed factor containing \(R-1\) ones must contain all but exactly one of the endpoint ones of \(W\). To end and begin with two zeros would require two zeros at the padded end and two following/preceding the last included one, but the nearest omitted endpoint one is only \(q-1=3\) positions away when \(q=4\). Explicitly, the prefix of length \(p_{R-1}+3=L-1\) leaves one left-padding zero, while the suffix case follows by reversal. Hence the missing label is indeed impossible.

**4. Count.** There are two endpoint classes and \(5(R-1)\) intermediate classes, minus one in the \(q=4\) exceptional case. This gives \(5R-3\) for \(q\ge5\) and \(5R-4\) for \(q=4\). For 2-Abelian equivalence, length-two counts depend only on \(K\), first symbol and last symbol because \(11\) is forbidden; the intermediate classes yield precisely the three pairs \((0,0),(0,1),(1,0)\), and the endpoints one each. Hence \(2+3(R-1)=3R-1\). \(\square\)

## Verification

The companion standalone `verify_cantor_3abelian.py` independently constructs finite iterates by both direct substitution and a base-\(q\) digit criterion. It directly counts *all eight* length-three pattern frequencies in every length-\(q^k\) factor of the next iterate and compares the complete observed label set with the theorem's classification. The verification covers \(q=4,5,6,7,8\) and every tested depth \(1\le k\le6\) satisfying \(q^{k+1}\le200000\), a total of 26 parameter pairs, and reports `VERIFY_OK cases=26`. The mathematical proof above supplies all-depth validity; finite tests are only cross-checks.

## Relationship to prior work

Lü, Chen, Guo and Wen's Cantor-like sequence paper [1] defines the same substitution family and derives ordinary factor and permutation complexity; those statistics count different equivalence relations and do not provide these 3-Abelian classes. Chen, Lü and Wu [2] study all-order Abelian complexity of the **ordinary** Cantor sequence (the \(q=3\) specialization), outside the present domain. Lü, Chen and Wen [3] study the **2-Abelian** complexity of generalized Cantor sequences, establishing regularity under conditions but not the finer 3-Abelian classification at these scales. The general notion of 3-Abelian equivalence is part of the theory in [4]. The new claim is not implied by the exact factor complexity in [1], a regularity assertion in [3], or the \(q=3\) result in [2]: it requires the complete third-order frequency/boundary reconstruction and a separate class realization theorem.

## Limitations

The theorem does not cover \(q=3\), arbitrary lengths, order-four Abelian classes, or the full 3-Abelian complexity sequence. The finite tests do not certify all parameters. Although relevant published texts were compared, a full-text assessment of [3] was not obtainable; an equivalent specialized result in its appendices or elsewhere remains an originality risk. No independent external scientific audit has been performed.

## References

[1] X.-T. Lü, J. Chen, Y.-J. Guo and Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110; first available online 2015-12-29. DOI: 10.1016/j.tcs.2015.12.022.

[2] J. Chen, X. Lü and W. Wu, *On the k-abelian complexity of the Cantor sequence*, arXiv:1703.04063 (2017).

[3] X.-T. Lü, J. Chen and Z.-X. Wen, *On the 2-abelian complexity of generalized Cantor sequences*, Theoretical Computer Science 936 (2022), 172–183. DOI: 10.1016/j.tcs.2022.09.025.

[4] J. Karhumäki, A. Saarela and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (2013).
