# Strict odd–positive-even occupancy covariance for diffuse unequal box probabilities

## Finding and scope

Independently allocate an integer \(n\ge2\) of labeled balls to finitely many boxes with probabilities \(p_i>0\), \(\sum_i p_i=1\). Write \(N_i\) for the load and \(U_i=\mathbf1\{N_i\text{ odd}\}\), \(V_i=\mathbf1\{N_i>0\text{ even}\}\). For every ordered pair of distinct boxes with \(p_i+p_j\le1/2\), one has \(\operatorname{Cov}(U_i,V_j)<0\). In particular, if **all** distinct pairs satisfy that bound, then the total counts \(O=\sum_i U_i\) and \(E=\sum_i V_i\) have \(\operatorname{Cov}(O,E)<0\). The result includes genuinely unequal vectors; for example \((1,2,3,3,3)/12\) satisfies the pair bound, including equality for some pairs. The within-box covariance is always strictly negative for \(n\ge2\) and two or more positive probabilities. For \(n=1\), \(E=0\).

## Proof

For distinct boxes put \(p=p_i\), \(q=p_j\), \(s=1-2p\), \(t=1-2q\), \(d=1-2p-2q\), and \(c=1-2p-q\). Their joint load generating polynomial is \(G(x,y)=(1-p-q+px+qy)^n\). Extract odd terms in \(x\) and even terms in \(y\) by evaluation at \(\pm1\), then subtract the odd terms at \(y=0\), which correspond to the empty box. This gives
\[
4\mathbb E[U_iV_j]=1+t^n-s^n-d^n-2(1-q)^n+2c^n.
\]
The marginals are \(\mathbb E U_i=(1-s^n)/2\), \(\mathbb E V_j=(1+t^n)/2-(1-q)^n\). Subtraction therefore gives
\[
4\operatorname{Cov}(U_i,V_j)=(st)^n-d^n+2c^n-2[s(1-q)]^n.
\]
Under the pair bound, \(d\ge0\). With \(\delta=2pq\) one has \(st=d+2\delta\), \(c=d+q\), and \(s(1-q)=c+\delta\). Since \(p<1/2\), \(0<\delta<q\), so \(d+2v<c+v\) for every \(0\le v\le\delta\). The function \(f(x)=x^n\) has strictly increasing derivative on \([0,\infty)\). Hence
\[
f(d+2\delta)-f(d)=2\int_0^\delta f'(d+2v)\,dv
<2\int_0^\delta f'(c+v)\,dv=2[f(c+\delta)-f(c)].
\]
This is the desired pair sign, including at \(d=0\). Within one box the two events are disjoint; each has positive probability (loads one and two both have positive probability). The covariance there is the negative product of their probabilities. Summing diagonal and ordered off-diagonal terms proves the total sign when all pair bounds hold.

## Verification

`python3 verify_parity_occupancy.py` uses weighted enumeration of labeled allocations for unequal rational vectors and compares each ordered-pair covariance to the parity formula. Checks include cases attaining the pair bound and strictly below it and also a qualifying pair in a vector that does not satisfy the bound for all pairs. This is finite corroboration; the proof is the exact generating-polynomial and derivative comparison above.

## Relation to other results and limits

The *Checkerboard covariance phases for parity and occupancy frequencies* result (Resultary record c6ffbeff2d78, Finding and even-frequency proof) supplies a stronger **uniform aggregate** sign via each even exact-load frequency, whose sum is \(E\). The result here is the pairwise inequality for distinct boxes of potentially different masses, and its aggregate consequence for unequal diffuse probabilities. The uniform aggregate sign, finite moment computation and uniform limit are not claimed as contributions here. Mao and Xue, arXiv:2608.23998, Eq. (10) and Theorem 2, give joint occupancy moments for independent uniform subset draws (their singleton case gives uniform allocation); the generating polynomial used here is elementary. Standard balls-in-bins negative association (Dubhashi–Ranjan, BRICS RS-96-25) concerns increasing functions, not these two parity indicators. This finding does not determine the aggregate sign when some pair exceeds the bound and does not assert negative association of the indicators.
