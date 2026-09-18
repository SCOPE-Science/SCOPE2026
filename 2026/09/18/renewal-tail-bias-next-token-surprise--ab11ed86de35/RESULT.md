# Exact renewal-tail bias and root-n window thresholds for next-token surprise

**Same-model review: passed. Cross-model review: not yet performed.**

## Result

Let \((X_t)_{t\in\mathbb Z}\) be a stationary marked renewal process in discrete time. Successive block lengths \(L_j\) are i.i.d. positive integers with
\[
\mu=\mathbb E L\in(0,\infty),
\]
and successive block marks \(Y_j\) are i.i.d. from an atomless distribution, independently of the lengths. Every time point in block \(j\) has value \(Y_j\). Thus distinct blocks have distinct observed values almost surely.

Fix an integer count threshold \(\zeta\ge0\). For \(n>\zeta\), define the next-token count-surprise probability
\[
S_{\le\zeta,n}
=
\mathbb P\!\left\{
N_{X_{n+1}}(X_1,\ldots,X_n)\le\zeta
\right\}.
\]
Then this target is independent of \(n\):
\[
\boxed{
S_{\le\zeta,n}=s_\zeta
=\frac{\mathbb E\min(L,\zeta+1)}{\mu}.
}
\]

Now use the one-sided leave-a-window-out construction of Nakul, Muthukumar and Pananjady (2026). For an integer window \(\tau\ge1\), set
\[
D_i=\{i,\ldots,(i+\tau-1)\wedge n\},\qquad
I_i=[n]\setminus D_i,
\]
and
\[
\widehat S_{\le\zeta,n}(\tau)
=
\frac1n\sum_{i=1}^n
\mathbf 1\!\left\{
N_{X_i}(X_{I_i})\le\zeta
\right\}.
\]

For every fixed \(\tau\),
\[
\boxed{
\widehat S_{\le\zeta,n}(\tau)
\longrightarrow
s_\zeta-
\frac{\zeta+1}{\mu}\,
\mathbb P(L>\tau+\zeta)
\quad\text{almost surely}.
}
\]
Hence the asymptotic downward bias is exactly
\[
\boxed{
B_\zeta(\tau)
=
\frac{\zeta+1}{\mu}\,
\mathbb P(L>\tau+\zeta).
}
\]

Consequently, a fixed window is asymptotically unbiased if and only if
\[
\mathbb P(L>\tau+\zeta)=0.
\]
In particular, for ordinary surprise \((\zeta=0)\),
\[
S_{0,n}=\frac1\mu,\qquad
B_0(\tau)=\frac{\mathbb P(L>\tau)}{\mu}.
\]
At \(\tau=1\), the estimator is the usual leave-one-out/Good--Turing singleton estimator, and
\[
\widehat S_{0,n}(1)\to\frac{\mathbb P(L=1)}{\mu}.
\]
Thus in this diffuse marked-renewal family Good--Turing is consistent for next-token surprise if and only if \(L=1\) almost surely.

### Growing windows: a root-\(n\) phase transition

Assume additionally
\[
\mathbb E L^2<\infty.
\]
Let \(\tau_n\to\infty\) satisfy \(\tau_n=o(\sqrt n)\), and put
\[
q_n=\mathbb P(L>\tau_n+\zeta).
\]
Define
\[
h_\zeta(\ell)=\min(\ell,\zeta+1),\qquad
\sigma_\zeta^2
=
\frac{\operatorname{Var}\!\left(
h_\zeta(L)-s_\zeta L
\right)}{\mu}.
\]
If
\[
\sqrt n\,q_n\to b\in[0,\infty),
\]
then
\[
\boxed{
\sqrt n\left(
\widehat S_{\le\zeta,n}(\tau_n)-s_\zeta
\right)
\Rightarrow
N\!\left(
-\frac{\zeta+1}{\mu}b,\,
\sigma_\zeta^2
\right).
}
\]
If instead \(\sqrt n\,q_n\to\infty\), then
\[
\sqrt n\left(
\widehat S_{\le\zeta,n}(\tau_n)-s_\zeta
\right)\to-\infty
\quad\text{in probability}.
\]

Thus the exact block-length tail, rather than a generic mixing-time surrogate, determines the centering scale:
\[
\boxed{
\sqrt n\,\mathbb P(L>\tau_n+\zeta)\to0
}
\]
is the sharp bias condition for the ordinary centered renewal-reward CLT in this family.

## Proof

### 1. Exact target from the equilibrium age law

Let \(A\) be the number of preceding time points in the block containing a stationary observation. The equilibrium renewal construction gives
\[
\mathbb P(A=a)=\frac{\mathbb P(L\ge a+1)}{\mu},
\qquad a=0,1,\ldots.
\]
Because the mark law is atomless, no other block has the same mark almost surely. Therefore
\[
N_{X_{n+1}}(X_1,\ldots,X_n)=\min(A,n).
\]
For \(n>\zeta\),
\[
S_{\le\zeta,n}
=
\sum_{a=0}^{\zeta}\frac{\mathbb P(L\ge a+1)}{\mu}
=
\frac{\mathbb E\min(L,\zeta+1)}{\mu}.
\]

### 2. Exact reward contributed by one complete block

Consider a complete block of length \(\ell\), and a point of rank \(r\in\{1,\ldots,\ell\}\) inside it. Away from the right sample boundary, deleting the forward window
\[
\{i,\ldots,i+\tau-1\}
\]
leaves exactly
\[
(r-1)+\max\{\ell-r-\tau+1,0\}
=
\max\{r-1,\ell-\tau\}
\]
copies of the same mark.

Hence the local count is at most \(\zeta\) exactly when
\[
r\le\zeta+1
\quad\text{and}\quad
\ell\le\tau+\zeta.
\]
Summing over all ranks in the block gives the deterministic block reward
\[
\boxed{
R_{\zeta,\tau}(\ell)
=
\min(\ell,\zeta+1)\,
\mathbf 1\{\ell\le\tau+\zeta\}.
}
\]

The renewal-reward theorem therefore gives, for fixed \(\tau\),
\[
\widehat S_{\le\zeta,n}(\tau)
\to
\frac{\mathbb E R_{\zeta,\tau}(L)}{\mu}
\quad\text{almost surely}.
\]
Initial and terminal partial blocks contribute \(o(n)\), and the fixed truncation of the final forward windows also contributes \(o(n)\).

Subtracting from \(s_\zeta\),
\[
s_\zeta-
\frac{\mathbb E R_{\zeta,\tau}(L)}{\mu}
=
\frac{
\mathbb E\!\left[
\min(L,\zeta+1)\mathbf 1\{L>\tau+\zeta\}
\right]}{\mu}.
\]
Since \(\tau\ge1\), the event \(L>\tau+\zeta\) implies \(L>\zeta+1\), so the minimum equals \(\zeta+1\). This yields
\[
B_\zeta(\tau)
=
\frac{\zeta+1}{\mu}\mathbb P(L>\tau+\zeta).
\]

### 3. Root-\(n\) growing-window law

Write
\[
h_\zeta(L)=\min(L,\zeta+1),\qquad
d_n(L)=(\zeta+1)\mathbf 1\{L>\tau_n+\zeta\}.
\]
For complete blocks, the triangular reward is
\[
R_n(L)=h_\zeta(L)-d_n(L),
\]
with time mean
\[
s_{\zeta,n}^{(\tau)}
=
\frac{\mathbb E R_n(L)}{\mu}
=
s_\zeta-\frac{\zeta+1}{\mu}q_n.
\]

The ordinary renewal-reward CLT for \(h_\zeta\) has asymptotic variance
\[
\sigma_\zeta^2
=
\frac{\operatorname{Var}(h_\zeta(L)-s_\zeta L)}{\mu}.
\]
Because \(q_n\to0\),
\[
d_n(L)-\frac{\zeta+1}{\mu}q_n L
\longrightarrow0
\]
in \(L^2\): the first term has second moment \((\zeta+1)^2q_n\), while the second is \(O(q_n)\) in \(L^2\) under \(\mathbb E L^2<\infty\). Thus replacing \(h_\zeta\) by \(R_n\) changes the centered regenerative fluctuation by \(o_p(1)\) on the \(\sqrt n\) scale.

The one-sided windows are truncated only for the final \(\tau_n\) sample positions, producing a deterministic discrepancy at most \(\tau_n/n=o(n^{-1/2})\). The initial and terminal partial renewal blocks are also \(o_p(n^{-1/2})\) after normalization. Hence
\[
\sqrt n\left(
\widehat S_{\le\zeta,n}(\tau_n)
-s_{\zeta,n}^{(\tau)}
\right)
\Rightarrow N(0,\sigma_\zeta^2).
\]
Finally,
\[
\sqrt n\left(
s_{\zeta,n}^{(\tau)}-s_\zeta
\right)
=
-\frac{\zeta+1}{\mu}\sqrt n\,q_n,
\]
which proves both the finite-shift limit and the divergent-bias statement.

## Consequences

### Geometric sticky blocks

Suppose
\[
\mathbb P(L=\ell)=p(1-p)^{\ell-1},\qquad \ell\ge1.
\]
Then \(\mu=1/p\) and
\[
\boxed{
s_\zeta=1-(1-p)^{\zeta+1},
}
\]
while the one-sided leave-a-window-out bias is exactly
\[
\boxed{
B_\zeta(\tau)
=
(\zeta+1)p(1-p)^{\tau+\zeta}.
}
\]
For ordinary surprise,
\[
s_0=p,\qquad B_0(\tau)=p(1-p)^\tau.
\]
Moreover
\[
\sigma_0^2=p(1-p).
\]
Therefore, along any integer window sequence satisfying
\[
\sqrt n(1-p)^{\tau_n}\to b,
\]
\[
\boxed{
\sqrt n\left(
\widehat S_{0,n}(\tau_n)-p
\right)
\Rightarrow
N(-pb,\;p(1-p)).
}
\]
The root-\(n\) window threshold is consequently centered at
\[
\tau_n\asymp
\frac{\log n}{2\log(1/(1-p))}.
\]

### Polynomial block tails

If
\[
\mathbb P(L>t)\sim C t^{-\alpha},
\qquad \alpha>2,
\]
then the root-\(n\) threshold occurs at
\[
\tau_n\asymp n^{1/(2\alpha)}.
\]
More precisely, if
\[
\tau_n\sim c\,n^{1/(2\alpha)},
\]
then
\[
\sqrt n\,q_n\to Cc^{-\alpha},
\]
and the limiting normal law has mean
\[
-\frac{\zeta+1}{\mu}Cc^{-\alpha}.
\]

### Bounded blocks

If \(L\le\ell_{\max}\) almost surely, then the asymptotic bias vanishes exactly once
\[
\tau+\zeta\ge\ell_{\max}.
\]
This gives an exact elbow: increasing the window further cannot improve asymptotic bias in the atomless marked-renewal model.

## Relation to prior work

Nakul, Muthukumar and Pananjady (2026) introduce one-sided leave-a-window-out estimation for next-token functionals and prove general parametric-rate error bounds under mixing and coupling assumptions. Their paper also emphasizes that leave-one-out can fail under temporal dependence. The result here does not claim the estimator, the surprise functional, or the general inconsistency phenomenon as new. It resolves a regenerative dependence family exactly and identifies the block-length survival probability at the window boundary as the complete asymptotic bias coordinate.

Pananjady, Muthukumar and Thangaraj (2024) introduced Windowed Good--Turing for stationary missing mass of Markov chains, with near-minimax risk guarantees, and extended it to small-count mass. Nakul, Muthukumar and Pananjady (2025) subsequently studied stationary mass frequency by frequency for mixing processes. Those works provide general-purpose risk control rather than the exact one-sided renewal-tail identity above.

Chandra, Thangaraj and Rajaraman (2022) study missing-mass estimation when i.i.d. symbols are repeated a geometrically distributed number of times, while Chandra and Thangaraj (2024) study missing mass under random duplications. These are the closest duplication-specific precedents. The present claim is restricted to the next-token count-surprise functional and the one-sided leave-a-window-out estimator in a stationary atomlessly marked renewal process.

To the best of our knowledge, the exact identity
\[
B_\zeta(\tau)
=
\frac{\zeta+1}{\mu}\mathbb P(L>\tau+\zeta),
\]
its necessary-and-sufficient fixed-window unbiasedness criterion, and the resulting root-\(n\) tail phase have not been stated in the inspected literature.

## Limitations

- Atomless marks are essential to the exact formulas because they rule out collisions between different renewal blocks. Finite or discrete mark alphabets introduce additional cross-block recurrence terms.
- The fixed-window law requires only \(\mathbb E L<\infty\), but the root-\(n\) statement assumes \(\mathbb E L^2<\infty\) and \(\tau_n=o(\sqrt n)\).
- The result is for the one-sided forward-window estimator used for next-token functionals. Symmetric WingIt windows have a different block combinatorics.
- The theorem gives exact bias and first-order fluctuation behavior for this regenerative family; it is not a minimax theorem over a broader dependence class.
- The full theorem/proof text of Chandra and Thangaraj, *Missing Mass Under Random Duplications* (ISIT 2024, DOI 10.1109/ISIT57864.2024.10619664), was not inspected. Because that paper is specifically about random duplication, an equivalent duplication-tail calculation there is the principal residual originality risk.

## References

1. M. Nakul, V. Muthukumar and A. Pananjady, *Next-token functional estimation*, arXiv:2609.19529 (2026).
2. A. Pananjady, V. Muthukumar and A. Thangaraj, *Just Wing It: Near-Optimal Estimation of Missing Mass in a Markovian Sequence*, Journal of Machine Learning Research 25 (2024), 1--43; arXiv:2404.05819.
3. M. Nakul, V. Muthukumar and A. Pananjady, *Estimating stationary mass, frequency by frequency*, arXiv:2503.12808 (2025).
4. P. Chandra, A. Thangaraj and N. Rajaraman, *Missing Mass Estimation from Sticky Channels*, IEEE ISIT 2022, 910--915; arXiv:2202.02772.
5. P. Chandra and A. Thangaraj, *Missing Mass Under Random Duplications*, IEEE ISIT 2024, 522--526, DOI:10.1109/ISIT57864.2024.10619664.
