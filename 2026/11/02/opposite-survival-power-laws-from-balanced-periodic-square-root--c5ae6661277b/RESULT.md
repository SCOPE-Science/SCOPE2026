# Opposite survival power laws from balanced periodic square-root perturbations

## Finding

The following single theorem describes a second-order survival exponent for periodically perturbed finite killed Markov chains. It includes a four-state example in which two starting cyclic classes have **opposite power-law corrections**, even though their exponential survival rate and every first-order block average coincide.

Let the objects and balance condition be as in the next section. Write \(P_r\) for the stationary \(d\)-step Doob kernel on a cyclic class, \(C_{r,h}\) and \(D_{r,h}\) for its first- and second-order block perturbations at time phase \(h\), and \(\pi_r\) for its stationary probability row. Let \(w_{r,h}\) be the unique zero-mass solution of
\[
 w_{r,h}(I-P_r)=\pi_r C_{r,h},\qquad w_{r,h}\mathbf 1=0.
\]
Under the **centering condition** \(\pi_r C_{r,h}\mathbf1=0\), define
\[
 \beta_{r,h}=\pi_r D_{r,h}\mathbf1+w_{r,h}C_{r,h}\mathbf1.
\]
For every fixed initial time \(m\ge1\), every \(x\in E_r\), and every terminal residue \(s\in\{0,\ldots,d-1\}\), there exists \(c_{m,x,s}>0\) such that, as \(n\to\infty\) with \(n-m\equiv s\pmod d\),
\[
 \mathbb P_{(m,x)}(n<\zeta)
 =\lambda^{n-m}n^{\beta_{r,m\bmod d}/d}
 \big(c_{m,x,s}+O(n^{-1/2})\big).
\]
The exponent includes a **linear-response term** \(wC\mathbf1\) in addition to the direct second-order term \(\pi D\mathbf1\); deleting it generally gives the wrong answer. The same coefficient admits the convergent Green-operator representation
\[
 \beta_{r,h}=\pi_rD_{r,h}\mathbf1+
 \sum_{j=0}^{\infty}\pi_r C_{r,h}P_r^j C_{r,h}\mathbf1.
\]
In particular, the complete construction below produces, for time \(m=2\) and initial states \(0\) and \(2\), respectively,
\[
 \mathbb P_{(2,0)}(n<\zeta)
 =3^{-(n-2)}n^{-3/160}(c_{0,s}+O(n^{-1/2})),
\]
\[
 \mathbb P_{(2,2)}(n<\zeta)
 =3^{-(n-2)}n^{3/32}(c_{2,s}+O(n^{-1/2})),
 \qquad s=(n-2)\bmod 2,
\]
with all constants strictly positive. The ratio of these two survival probabilities grows at order \(n^{9/80}\), with a positive residue-dependent multiplier.

## Assumptions and scope

Take a finite state set \(E\), a nonzero irreducible substochastic matrix \(K\) with at least one row sum strictly less than one, and its Perron eigenpair \(KR=\lambda R\), \(R>0\), \(0<\lambda<1\). Let \(d\) denote its period, with cyclic decomposition \(E_0,\ldots,E_{d-1}\). Let
\[
 Q(x,y)=\frac{K(x,y)R(y)}{\lambda R(x)}
\]
be the stochastic Doob matrix. For each \(r\), \(P_r=Q^d|_{E_r\times E_r}\) is primitive and has stationary probability row \(\pi_r\).

At each integer time \(n\ge1\), let \(K_n\) be a substochastic matrix with the **same positive-entry support** as \(K\). Assume bounded real edge arrays \(a_0,\ldots,a_{d-1}\) and \(b_0,\ldots,b_{d-1}\) satisfy, uniformly over supported edges,
\[
 \frac{K_n(x,y)}{K(x,y)}
 =1+\frac{a_{n\bmod d}(x,y)}{\sqrt n}
 +\frac{b_{n\bmod d}(x,y)}{n}+O(n^{-3/2}).
\]
All times and starts are integer valued; the perturbation phase is indexed by **absolute time**. Define \(A_h(x,y)=K(x,y)a_h(x,y)\), \(B_h(x,y)=K(x,y)b_h(x,y)\), and \(h=m\bmod d\). For a matrix on \(E\), a subscript \([r]\) means restriction to \(E_r\times E_r\). Define
\[
 \mathcal C_{r,h}=
 \left[\sum_{j=0}^{d-1}K^jA_{(h+j)\bmod d}K^{d-1-j}\right]_{[r]},
\]
\[
 \mathcal D_{r,h}=
 \left[\sum_{j=0}^{d-1}K^jB_{(h+j)\bmod d}K^{d-1-j}
 +\sum_{0\le j<k<d}K^jA_{(h+j)\bmod d}K^{k-j-1}A_{(h+k)\bmod d}K^{d-1-k}\right]_{[r]}.
\]
With \(H_r=\operatorname{diag}(R|_{E_r})\), set
\[
 C_{r,h}=\lambda^{-d}H_r^{-1}\mathcal C_{r,h}H_r,
 \qquad D_{r,h}=\lambda^{-d}H_r^{-1}\mathcal D_{r,h}H_r.
\]
The asserted asymptotics require \(\pi_r C_{r,h}\mathbf1=0\) for the indicated starting class and time phase. No centering is asserted for arbitrary inputs; without it there can be a stretched-exponential factor.

## Proof

**1. Block expansion and centering.** Set \(T_j=m+jd\). Since \((T_j+k)^{-1/2}=T_j^{-1/2}+O(T_j^{-3/2})\) and \((T_j+k)^{-1}=T_j^{-1}+O(T_j^{-2})\) for fixed \(k\), multiplication of the \(d\) consecutive kernels gives
\[
 K_{T_j}\cdots K_{T_j+d-1}\big|_{[r]}
 =K^d\big|_{[r]}+T_j^{-1/2}\mathcal C_{r,h}
 +T_j^{-1}\mathcal D_{r,h}+O(T_j^{-3/2}).
\]
The similarity transformation by \(H_r\) and division by \(\lambda^d\) produces the positive block matrices
\[
 M_j=P_r+T_j^{-1/2}C_{r,h}+T_j^{-1}D_{r,h}
 +O(T_j^{-3/2}).
\]
Every block begins at the same phase \(h\); the displayed \(A_jA_k\) term is indispensable.

**2. Perturbed stationary probability row.** Suppress the indices \(r,h\). Starting with the probability row \(v_0\) concentrated at the chosen state, let
\[
 S_j=v_0M_0\cdots M_{j-1}\mathbf1,\qquad
 v_j=\frac{v_0M_0\cdots M_{j-1}}{S_j}.
\]
All \(S_j\) are positive. The recursion \(v_{j+1}=v_jM_j/(v_jM_j\mathbf1)\) and primitivity of \(P\) imply \(v_j=\pi+O(T_j^{-1/2})\). Indeed, some fixed power of \(P\) contracts zero-mass rows in total variation and the perturbation of that fixed-block map is \(O(T_j^{-1/2})\); iterating the contraction gives this bound.

The equation \(w(I-P)=\pi C\), \(w\mathbf1=0\), has a unique solution: the right side has mass zero by centering, and \(I-P\) is invertible on zero-mass rows. Substitute \(v_j^*=\pi+T_j^{-1/2}w\) into the normalized recursion. Its first-order term is
\[
 \pi+T_j^{-1/2}(wP+\pi C)+O(T_j^{-1})
 =\pi+T_j^{-1/2}w+O(T_j^{-1}).
\]
The time shift \(T_{j+1}^{-1/2}-T_j^{-1/2}=O(T_j^{-3/2})\). A fixed-block contraction applied to the residual therefore gives the sharper estimate
\[
 v_j=\pi+T_j^{-1/2}w+O(T_j^{-1}).
\]
This step supplies the response term that cannot be obtained merely by averaging single-time killing rates.

**3. Scalar growth and terminal residues.** The normalized multiplier is
\[
 \frac{S_{j+1}}{S_j}=v_jM_j\mathbf1
 =1+\frac{\pi D\mathbf1+wC\mathbf1}{T_j}+O(T_j^{-3/2})
 =1+\frac{\beta}{T_j}+O(T_j^{-3/2}).
\]
Taking logarithms, summing the convergent error series, and using \(\sum_{k<j}(m+kd)^{-1}=d^{-1}\log j+\text{constant}+O(j^{-1})\), yields
\[
 S_j=c\,T_j^{\beta/d}(1+O(T_j^{-1/2}))
\]
for some \(c>0\). The similarity identity for the original kernels contributes \(\lambda^{jd}\) and a positive terminal vector \(R^{-1}\). For an additional fixed \(s\) steps, the h-transformed product tends to \(Q^s\), so the terminal factor tends to \(\pi_r Q^s[R^{-1}]>0\), with error \(O(T_j^{-1/2})\). Replacing \(T_j\) by the terminal time \(n\) gives the claimed asymptotic, with a positive constant for each residue.

**4. Green representation.** On zero-mass row vectors, the series \(\sum_{j\ge0}P^j\) is the inverse of \(I-P\), since \(P\) is primitive. Hence \(w=\sum_{j\ge0}\pi CP^j\), and substituting this into \(wC\mathbf1\) gives the stated absolutely convergent series. This expression includes autocorrelation through the block dynamics rather than just the direct quadratic perturbation.

**5. Explicit sign-split example.** Take \(E=\{0,1,2,3\}\), \(\lambda=1/3\), \(K=\lambda Q\) and
\[
 Q=\begin{pmatrix}
 0&0&3/4&1/4\\
 0&0&1/4&3/4\\
 2/3&1/3&0&0\\
 1/3&2/3&0&0
 \end{pmatrix}.
\]
For \(n\ge1\), put
\[
 K_n=\tfrac13\operatorname{diag}\left(
 1+\frac{f_{n\bmod2}(i)}{4\sqrt n}:i\in E
 \right)Q,
 \quad f_0=(1,-1,1,-1),\quad f_1=(2,-2,-1,1).
\]
Every positive entry remains positive because the diagonal factors lie in \([1/2,3/2]\), and all row sums lie in \([1/6,1/2]\). The period is two, the cyclic classes are \(E_0=\{0,1\}\) and \(E_1=\{2,3\}\), and \(R=\mathbf1\). Fix an even starting time. The block expansion is \(P_r=Q^2|_{[r]}\), \(C_{r,0}=(A_0Q+QA_1)|_{[r]}\), \(D_{r,0}=(A_0A_1)|_{[r]}\), with \(A_h=\frac14\operatorname{diag}(f_h)Q\). Both stationary rows are \((1/2,1/2)\). Exact rational calculation yields

| Starting class | \(\pi C\mathbf1\) | \(w\) | \(\pi D\mathbf1\) | \(wC\mathbf1\) | \(\beta\) |
|---|---:|---|---:|---:|---:|
| \(E_0\) | \(0\) | \((-1/40,1/40)\) | \(-1/32\) | \(-1/160\) | \(-3/80\) |
| \(E_1\) | \(0\) | \((7/40,-7/40)\) | \(1/24\) | \(7/48\) | \(3/16\) |

Divide \(\beta\) by the two-step period. This proves exponents \(-3/160\) and \(3/32\), without asymptotic inference from numerics. The identical calculation for odd absolute starting phase interchanges the exponents between the classes.

## Verification

The accompanying standard-library-only script `verify.py` computes every example coefficient using exact fractions, checks both starting phases and both cyclic classes, confirms centering and the zero-mass Poisson equation, and compares the second-order product coefficients with an independent formal matrix expansion. It also computes finite-horizon normalized survival log-slopes, which are diagnostics rather than proofs. The recorded run in `verification_output.txt` passed \(56\) assertions. The general infinite-time theorem is justified by the contraction and convergent product arguments above.

## Relationship to prior work

Kohki Iba's 2026 paper proves survival and conditioning asymptotics for finite time-inhomogeneous killed chains under a **time-independent** leading \(1/n\) perturbation with a \(1/n^2\) remainder. Its survival correction exponent is a single stationary average \(\kappa\) across cyclic classes. The present hypotheses instead have a centered, periodically phased \(1/\sqrt n\) leading term, whose *quadratic* response can yield distinct class exponents; Iba's stated expansion excludes these examples.

Champagnat and Villemonais study periodic absorbed **time-homogeneous** chains, and hence do not give these time-decaying perturbation exponents. General asymptotic integration of matrix difference systems, including Benzaid–Lutz, could supply a more abstract alternative derivation of some steps; the specific Markov-chain formula and the sign-splitting example are not established by the accessible abstract. This general-theory priority issue has not been definitively settled.

## Limitations

The theorem is for finite state spaces, kernels of fixed support, and a perturbation phase synchronized with the period of the limiting kernel. The zero first-order block average is essential: unbalanced perturbations are outside the power-law statement. The proof gives positive but not elementary closed forms for the leading constants. It does not assert any new result for arbitrary infinite-state chains, random environments, or pathwise survival times beyond the stated one-time probabilities. The full mathematical priority of the second-order response formula relative to general difference-equation asymptotics remains a residual literature question.

## References

1. Kohki Iba, *Finite-State Time-Inhomogeneous Markov Chains Conditioned to Survive*, arXiv:2610.38590v1, 28 October 2026, https://arxiv.org/html/2610.38590v1 .
2. Nicolas Champagnat and Denis Villemonais, *Quasi-limiting estimates for periodic absorbed Markov chains*, arXiv:2211.02706, first posted 4 November 2022, https://arxiv.org/abs/2211.02706 .
3. Z. Benzaid and D. A. Lutz, *Asymptotic Representation of Solutions of Perturbed Systems of Linear Difference Equations*, Studies in Applied Mathematics 77 (1987), 195–221, https://doi.org/10.1002/sapm1987773195 .
