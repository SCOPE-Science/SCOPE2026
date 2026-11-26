# Independent mathematical audit

## correctness

PASS

The claim uses one Bernoulli choice per step to reset the pair jointly, independent across time, as specified in Assumptions; it is not a model with separate coins for the two qubits. In the plus/minus basis of the second qubit, H has a plus block with eigenvalues 0 and 8, and a minus block 2 times the Pauli Y. Exponentiating gives the stated real quarter-turn matrix; its square is I tensor X. The channel contracts trace distance by q=1-p and its four-step renewal sum has weights (1,q,q^2,q^3)/Z with Z=(1+q)(1+q^2). Independent check of concurrence: write rho=XX^T with real weighted orbit columns. X^T S X has the same nonzero squared eigenvalues as the spin-flip product, by the AB/BA identity. Removing the null direction in the two even orbit columns gives the real symmetric matrix with rows (0,-a,b), (-a,-v,0), (b,0,w), where v=q/Z, w=q^3/Z, a^2=(1+q^2)q/(4Z^2), b^2=(1+q^2)q^3/(4Z^2). Its determinant is a^2 w-b^2 v=0, and the lower principal minor -vw is negative. Its two nonzero eigenvalues have opposite signs, so the difference of their absolute values in Wootters' formula is |w-v|. The sum of their squares is v^2+w^2+2(a^2+b^2) and their squared product is (vw+a^2+b^2)^2, agreeing with the frozen spectral coefficients. Reversing the odd orbit columns' weights interchanges v and w in this calculation. The half-turn stationary state is a mixture of two product basis states. The derivative in q has numerator 1-2q-q^2, has exactly one interior zero, and the endpoint concurrence limits are both zero, yielding p*=2-sqrt(2) and (sqrt(2)-1)/2.

## originality

PASS

The supported distinct claim is the exact odd-quarter-turn concurrence law and unique optimizer over the reset probability. Neither the gate, the resonances, the renewal state, nor entanglement without a positive reset threshold is new on the evidence examined. The half-turn separability is a direct consequence of the known gate and renewal mixture.

## value

PASS

An exact entanglement curve for a previously numerically studied resonant gate answers a natural control question: it gives the unique reset probability that maximizes the stationary concurrence and quantifies the cost of other rates. The spin-flip rank and cancellation supply quantitative information not available from a sign or limiting calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
