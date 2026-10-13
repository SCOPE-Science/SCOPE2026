# A high-noise counterexample to the five-message Z-channel recursion at length eight
## Finding
Consider the length-eight, five-message codebook conjectured to be optimal for the binary Z-channel by Chen, Lin, and Moser (2011, equation (26); 2013, equation (89)). Written as five binary rows in the published column order, it is
\[
C_{\mathrm{rec}}=\{00000000,\ 00100101,\ 01001010,\ 10010011,\ 11111111\}.
\]
The alternative codebook
\[
C_{\mathrm{dis}}=\{00000000,\ 11000000,\ 00111000,\ 00000111,\ 11111111\}
\]
uses the same five-message alphabet and length and is assembled solely from the first three weak-flip column vectors appearing in the original paper.

Let \(p\in(0,1)\) be the probability that a transmitted \(1\) becomes \(0\); a transmitted \(0\) is never altered. Messages are uniform, and decoding uses maximum likelihood. Writing \(P_{\mathrm c}(C;p)\) for average correct-decoding probability, the exact formulas for all \(0<p<1\) are
\[
\begin{aligned}
5P_{\mathrm c}(C_{\mathrm{rec}};p)&=5-4p^3-2p^5+2p^7,\\
5P_{\mathrm c}(C_{\mathrm{dis}};p)&=5-p^2-2p^3-2p^5-p^6+2p^8.
\end{aligned}
\]
Consequently,
\[
5\bigl(P_{\mathrm c}(C_{\mathrm{dis}};p)-P_{\mathrm c}(C_{\mathrm{rec}};p)\bigr)
=p^2(1-p)^2(1+p)(2p^3+p-1).
\]
The polynomial \(2p^3+p-1\) has a unique root \(\rho\in(0,1)\), with \(\rho\approx0.5897545123\). Hence the proposed recursive codebook is **strictly suboptimal** for every \(\rho<p<1\). For instance, at \(p=9/10\), the alternative reduces the average decoding-error probability by exactly \(1044981/250000000\).

## Assumptions and scope
Each codebook contains exactly five distinct length-eight binary codewords, all messages are equiprobable, and the channel acts independently on coordinates. Its transition law is
\[
\Pr(Y=y\mid X=x)=
\begin{cases}
p^{|x|-|y|}(1-p)^{|y|},&\operatorname{supp}(y)\subseteq\operatorname{supp}(x),\\
0,&\text{otherwise}.
\end{cases}
\]
For an ML decoder, the correct-decoding probability is
\[
P_{\mathrm c}(C;p)=\frac15\sum_{y\in\{0,1\}^8}
\max_{x\in C}\Pr(Y=y\mid X=x).
\]
When likelihoods tie, any tie-breaking rule yields this same averaged success probability. The statement concerns actual finite-blocklength ML probability, not asymmetric-distance correction or a union bound. No global optimality is asserted for the alternative.

## Proof
The column vectors in the 2011 paper, in the order used here, are
\[
\begin{aligned}
c_1&=(0,0,0,1,1)^T,&c_2&=(0,0,1,0,1)^T,\\
c_3&=(0,1,0,0,1)^T,&c_4&=(0,0,1,1,1)^T,\\
c_5&=(0,1,0,1,1)^T.
\end{aligned}
\]
The exact proposed base case is the column sequence \((c_1,c_2,c_3,c_1,c_2,c_3,c_4,c_5)\), whose rows equal \(C_{\mathrm{rec}}\). The competing column sequence \((c_3,c_3,c_2,c_2,c_2,c_1,c_1,c_1)\) has rows \(C_{\mathrm{dis}}\).

Fix \(0<p<1\) and an output \(y\) of weight \(w\). Among codewords containing the support of \(y\), the likelihood is \(p^{m-w}(1-p)^w\), with \(m\) the transmitting word's weight. Since \(p<1\), the maximal likelihood comes from the *smallest* such \(m\), independently of \(p\). Thus an exact partition of the output supports by minimum covering codeword weight computes the ML success probability for the entire open parameter interval.

For \(C_{\mathrm{dis}}\), the three nonzero middle codewords have disjoint supports of sizes \(2,3,3\), covering all eight coordinates; the two remaining words are the empty support and the full support. If the middle support sizes are \(a_1,a_2,a_3\), their contributions to \(5P_{\mathrm c}\) are \(1-p^{a_i}\). The zero word contributes \(1\), and the all-one word contributes \(1+2p^8-\sum_i p^{8-a_i}\), after excluding the output supports already assigned to the four lighter words. Hence
\[
5P_{\mathrm c}(C_{\mathrm{dis}};p)
=5+2p^8-\sum_{i=1}^3(p^{a_i}+p^{8-a_i})
=5-p^2-2p^3-2p^5-p^6+2p^8.
\]

For \(C_{\mathrm{rec}}\), let \(A,B,D\) be the supports of the three middle words, with sizes \(3,3,4\). They satisfy \(A\cap B=\varnothing\), and each of \(A\cap D\) and \(B\cap D\) consists of a distinct singleton. The zero word contributes \(1\); the two weight-three words contribute \(1-p^3\) each; and the weight-four word contributes \(1-p^4-2p^3(1-p)\), because each of those two singleton outputs is instead decoded as a lighter word. The all-one word contributes
\[
1-p^8-2p^5(1-p^3)-p^4(1-p^4)+2p^7(1-p).
\]
Adding these five contributions and simplifying yields
\[
5P_{\mathrm c}(C_{\mathrm{rec}};p)=5-4p^3-2p^5+2p^7.
\]
Subtracting and multiplying out gives the factorization in the finding. Since the derivative of \(2p^3+p-1\) equals \(6p^2+1>0\), and its values at \(0\) and \(1\) have opposite signs, it has exactly one root in \((0,1)\). Every other factor is strictly positive for \(0<p<1\). This proves strict improvement throughout \((\rho,1)\).

At \(p=9/10\), the two values of \(5P_{\mathrm c}\) are, respectively,
\[
\frac{9298069}{5000000}
\quad\text{and}\quad
\frac{94025671}{50000000}.
\]
The positive difference in **actual** success probabilities is their difference divided by \(5\), namely \(1044981/250000000\).

## Verification
The self-contained `verify.py` uses only the Python standard library. It reconstructs the two codebooks from the five original column vectors, evaluates all \(256\) possible received words, and produces exact integer-coefficient ML-success polynomials. A separate direct maximum-over-codewords calculation at six rational channel probabilities agrees with those polynomials and with the formulas proved above. It also checks the rational gap at \(p=9/10\) and brackets the unique root between \(0.5897\) and \(0.5898\). Run `python3 verify.py`; expected terminal output is included as `verification_output.txt`.

## Relationship to prior work
Chen, Lin, and Moser (2011), Section IV-B and equations (25)–(26), proposed \(C_{\mathrm{rec}}\) as the base of their conjecturally optimal recursion for five codewords on the Z-channel. Their expanded 2013 treatment repeats the same conjecture in Section IV-E and equations (88)–(90). The paper proves optimality for two through four messages, but expressly presents the five-message construction as conjectural. The new statement is a direct exact-probability counterexample to the **five-message** claim, not a reproof of their established cases.

The alternative belongs to the authors' own weak-flip column family. This isolates the failure to the particular choice of column multiplicities for the length-eight base case, rather than changing the channel, message distribution, decoding rule, or permissible column alphabet.

## Limitations
The comparison disproves optimality only where \(\rho<p<1\), although both success polynomials are valid for all \(0<p<1\). It does not prove that \(C_{\mathrm{dis}}\) is globally optimal, decide the exact ML optimum at any parameter, settle the proposed odd-length branch, or classify higher lengths. Other equivalent or historically unindexed counterexamples may exist. No independent external audit has been conducted.

## References
1. P.-N. Chen, H.-Y. Lin, and S. M. Moser, “Ultra-Small Block-Codes for Binary Discrete Memoryless Channels,” IEEE Information Theory Workshop, pp. 175–179 (2011), DOI: 10.1109/ITW.2011.6089371. Author-hosted full text: https://moser-isi.ethz.ch/docs/papers/chen-lin-smos-2011-5.pdf. Earliest verified public bibliographic date: 2011-12-21.
2. P.-N. Chen, H.-Y. Lin, and S. M. Moser, “Optimal Ultrasmall Block-Codes for Binary Discrete Memoryless Channels,” IEEE Transactions on Information Theory, 59(11), 7346–7378 (2013), DOI: 10.1109/TIT.2013.2276893. Author-hosted full text: https://moser-isi.ethz.ch/docs/papers/chen-lin-smos-2013-1.pdf.
