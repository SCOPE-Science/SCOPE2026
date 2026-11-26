# Uniform mean-square amplification under fresh reshuffling of two stable heavy-ball epoch orders

## Finding

There are two strictly convex scalar quadratic losses with a common minimizer and exact rational heavy-ball parameters for which both frozen epoch orders converge with spectral radius \(1/2\), but an independent fair choice of order gives the uniform conditional bound
\[
\mathbb E[\|Z_{k+1}\|_2^2\mid Z_k=z]\ge \frac{49}{2}\|z\|_2^2\qquad(z\in\mathbb R^2).
\]
In particular \(\mathbb E\|Z_k\|_2^2\ge (49/2)^k\|Z_0\|_2^2\) for every starting state. The bound concerns the full two-coordinate momentum state and uses the same step size and two gradient evaluations per epoch for the frozen and reshuffled protocols. Unlike a comparison of spectral radii of second-moment operators, it certifies expansion in the specified norm from every input state already in one epoch.

## Model and proof

Use losses \(x^2/2\) and \(10x^2/2\), step size \(\eta=31/20\) and momentum \(\beta=1/2\). Each gradient evaluation with curvature \(c\in\{1,10\}\) updates \(x_{j+1}=x_j-\eta c x_j+\beta(x_j-x_{j-1})\). Momentum is not reset between epochs; \(Z_k=(x_{2k},x_{2k-1})^{\mathsf T}\) samples the state once per epoch. With \(T_c=\left(\begin{smallmatrix}1+\beta-\eta c&-\beta\\1&0\end{smallmatrix}\right)\), the two epoch maps are
\[
P=T_{10}T_1=\begin{pmatrix}1/5&7\\-1/20&-1/2\end{pmatrix},\qquad
Q=T_1T_{10}=\begin{pmatrix}1/5&1/40\\-14&-1/2\end{pmatrix}.
\]
Both have characteristic polynomial \(s^2+(3/10)s+1/4\), whose simple roots \((-3\pm i\sqrt{91})/20\) have modulus \(1/2\). Repeating either order therefore gives geometric decay of the epoch state from every starting state (the bound has an order-dependent prefactor).

Under independent equiprobable reshuffling the next squared state norm has conditional expectation \(z^{\mathsf T}Kz\), where
\[
K=\tfrac12(P^{\mathsf T}P+Q^{\mathsf T}Q)=
\begin{pmatrix}78433/800&843/200\\843/200&79201/3200\end{pmatrix}.
\]
The leading entry and determinant of \(K-(49/2)I\) are \(58833/800\) and \(1643697/2560000\); both are positive. Sylvester's criterion proves the conditional bound, and iterated expectation proves the all-epoch bound.

## Verification

Run `python3 verify.py` to reconstruct the two epoch maps, characteristic polynomial and positive-definiteness certificate in exact rational arithmetic. The script also checks trace and determinant identities on a rational grid as supplementary fixed-order checks. The conditional expectation proof, not a trajectory simulation or grid, establishes the all-state bound.

## Relation to other results and limitations

The component-update rule and independent permutations agree with the no-Nesterov, batch-size-one specialization of Algorithm 1 in Qiu, Ma and Milzarek, *Random Reshuffling with Momentum: Complexity Bounds and Last-iterate Convergence*, [arXiv:2404.18452v3](https://arxiv.org/abs/2404.18452v3). The cyclic stability diagram is not claimed here; see the earlier [fixed-order diagram](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-a-sharp-disconnected-stability-diagram-for-cyclic-two-component--60f51dc1b1a2/RESULT.md). Single-shuffle versus fresh reshuffling for batch-normalized SGD ([arXiv:2302.12444](https://arxiv.org/abs/2302.12444)) and epoch-level Shuffling Momentum Gradient ([PMLR 139, 2021](https://proceedings.mlr.press/v139/tran21b.html)) use different updates.

The abstract indexed at [OpenReview tQwrBw2Lcm](https://openreview.net/forum?id=tQwrBw2Lcm) also describes stability of frozen heavy-ball orders and instability of fresh reshuffling, in a regime with Schur-stable individual component maps. The full theorem was not compared. Stable individual component maps for \(0\le\beta<1\) have \(|d_c|<1+\beta\) for \(d_c=1+\beta-\eta c\), by the quadratic Schur criterion. In that regime the conditional expansion on the second coordinate unit vector is \(K_{22}=\beta^2(1+(d_1^2+d_{10}^2)/2)<5\); thus stability of the individual maps cannot be imposed on a witness of the uniform factor \(49/2\). No priority is claimed for the qualitative frozen/reshuffled separation. The certificate is in the Euclidean norm on the two ordered iterates, not a coordinate-invariant amplification factor. It does not give almost-sure divergence, general learning-rate regions, or stability results for nonquadratic or multidimensional losses.
