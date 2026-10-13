# A separable two-qubit counterexample to oblique-discord mutual-information monotonicity

## Finding

Xu's 2015 equation-(22) conjecture asserts that a normalized dual-basis operation cannot increase bipartite mutual information. The assertion fails in the smallest nontrivial bipartite dimension, even when the initial state already has zero oblique discord.

Specifically, on \(\mathbb C^2\otimes\mathbb C^2\), set
\[
|u\rangle=\frac{15|0\rangle+8|1\rangle}{17},\qquad
\rho=\frac14|0,0\rangle\langle0,0|+\frac34|u,1\rangle\langle u,1|.
\]
For the normalized nonorthogonal basis
\[
|v_0\rangle=|0\rangle,\qquad
|v_1\rangle=\frac{4|0\rangle+3|1\rangle}{5},
\]
let \(\Phi_A\) be Xu's equation-(13) operation. Then
\[
I(\Phi_A\rho)-I(\rho)
=0.05728010640002332764\ldots\quad\text{bits}>0.
\]
Moreover, a rational interval certificate establishes the strict gap
\[
\left[I(\Phi_A\rho)-I(\rho)\right]\ln2>\frac1{30}.
\]
The state \(\rho\) is zero-oblique-discord by Xu's equation-(12) definition, using the normalized basis \(\{|0\rangle,|u\rangle\}\) and the orthogonal states \(|0\rangle,|1\rangle\) of the other qubit. Consequently the proposed information-theoretic infimum in equation (21) is **strictly negative** at this state.

## Assumptions and scope

All kets and matrices are expressed in the standard computational basis; all state entropies and mutual information use base-two logarithms. For a normalized basis \(\{|v_i\rangle\}_{i=0,1}\) and its unique biorthogonal dual \(\{|\widetilde v_i\rangle\}\), the operation is precisely
\[
\Phi_A(\rho)
=\frac{\sum_{i=0}^{1}(K_i\otimes I)\rho(K_i^\dagger\otimes I)}
{\operatorname{Tr}\sum_{i=0}^{1}(K_i\otimes I)\rho(K_i^\dagger\otimes I)},
\qquad K_i=|v_i\rangle\langle\widetilde v_i|.
\]
It is nonlinear through its state-dependent normalization and must not be confused with deterministic completely positive trace-preserving dephasing. All probabilities in the example are positive and both relevant Alice bases are linearly independent and individually normalized.

## Proof

The biorthogonal dual vectors are
\[
|\widetilde v_0\rangle=|0\rangle-\frac43|1\rangle,\qquad
|\widetilde v_1\rangle=\frac53|1\rangle,
\]
so
\[
K_0=\begin{pmatrix}1&-4/3\\0&0\end{pmatrix},\qquad
K_1=\begin{pmatrix}0&4/3\\0&1\end{pmatrix}.
\]
Each \(K_i\) is exactly Xu's rank-one dual-basis Kraus operator. The unnormalized conditional Alice state obtained from \(|u\rangle\langle u|\) is
\[
\sigma=\sum_i K_i|u\rangle\langle u|K_i^\dagger
=\begin{pmatrix}1193/2601&256/867\\256/867&64/289\end{pmatrix},
\qquad\operatorname{Tr}\sigma=\frac{1769}{2601}.
\]
The global normalization is \(Z=\frac14+\frac34\operatorname{Tr}\sigma=659/867\), so the transformed state is a classical mixture on Bob with the \(|1\rangle\) probability
\[
q=\frac{1769}{2636}
\]
and the conditional state
\[
\sigma_1=\sigma/\operatorname{Tr}\sigma
=\frac1{1769}\begin{pmatrix}1193&768\\768&576\end{pmatrix}.
\]
The input and output Alice marginals are
\[
\rho_A=\frac1{289}\begin{pmatrix}241&90\\90&48\end{pmatrix},\qquad
\rho_A'=\frac1{659}\begin{pmatrix}515&192\\192&144\end{pmatrix}.
\]
Their respective characteristic discriminants are \(241/289\), \(285097/659^2\), and \(2739985/1769^2\) for \(\rho_A,\rho_A',\sigma_1\). Define \(h(t)=-t\log_2t-(1-t)\log_2(1-t)\). Since the Bob registers are orthogonal and the initial Alice conditionals are pure,
\[
I(\rho)=h\!\left(\frac{1+\sqrt{241}/17}{2}\right).
\]
By the exact entropy formula for a state classical on Bob,
\[
I(\Phi_A\rho)
=h\!\left(\frac{1+\sqrt{285097}/659}{2}\right)
-\frac{1769}{2636}
 h\!\left(\frac{1+\sqrt{2739985}/1769}{2}\right).
\]
The strict increase follows by an exact-rational interval proof, not by treating displayed decimals as certificates. The standalone verifier `verify.py` bounds each radical using the integer square root at scale \(10^{10}\), encloses each natural logarithm through the convergent identity
\[
\ln y=2\sum_{j=0}^{n-1}\frac{z^{2j+1}}{2j+1}+R_n,
\qquad z=\frac{y-1}{y+1},\qquad
0\le R_n\le\frac{2z^{2n+1}}{(2n+1)(1-z^2)}
\]
for \(1\le y<2\), with dyadic argument reduction and \(n=12\). Exact rational arithmetic then proves that the natural-logarithm entropy difference is larger than \(1/30\) (and smaller than \(1/20\)) nat.

Finally \(K_0^\dagger K_0+K_1^\dagger K_1\) has exact eigenvalues \(5,5/9\). Thus replacing each \(K_i\) by \(K_i/\sqrt5\) yields a legitimate trace-nonincreasing completely positive success branch; conditioning on success gives the same \(\Phi_A\rho\). Ordinary deterministic data-processing inequalities do not cover such postselection.

## Verification

Run `python3 verify.py` using Python's standard library. It reconstructs both dual-basis operators and all stated density matrices over \(\mathbb Q\), checks their exact traces and characteristic discriminants, and certifies the entropy inequality with rational upper and lower endpoints. No floating-point operation is used in the decision criterion; decimal approximations are illustrative only.

## Relationship to prior work

Xu's preprint *Oblique discord* [1] defines zero-oblique-discord states in equation (12), the normalized operation in equation (13), the information-theoretic candidate in equation (21), and poses the mutual-information monotonicity conjecture in equation (22). The example contradicts exactly that statement rather than a different, unnormalized mapping. General deterministic local-channel data processing does not imply it because the operation conditions on an outcome. Prior literature on local filtering, including [2], treats filtering effects on quantum correlations, but its investigated freezing behavior does not establish the universal inequality for Xu's restricted dual-basis maps or exhibit this exact zero-oblique-discord witness.

## Limitations

Only a finite two-qubit witness and its exact information increase are claimed. The example does not classify all dual-basis maps, states, or extrema. The strict gap is for the normalized branch and makes no assertion of a deterministic-channel violation; the normalized map may be state-dependent. The searched literature does not exclude unindexed or differently named equivalent counterexamples. No independent audit has been performed.

## References

[1] Jianwei Xu, *Oblique discord*, arXiv:1506.00404v1 (publicly posted 2015-06-01), equations (12), (13), (21), (22); later journal version DOI:10.1142/S0217979216502568.

[2] Sumana Karmakar, Ajoy Sen, Amit Bhar, Debasis Sarkar, *Effect of local filtering on Freezing Phenomena of Quantum Correlation*, arXiv:1504.05231v1 (2015); related filtering context, not an assertion covering the present map or counterexample.
