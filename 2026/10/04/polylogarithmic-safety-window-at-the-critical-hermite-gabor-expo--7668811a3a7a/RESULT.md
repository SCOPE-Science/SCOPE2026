# Polylogarithmic safety window at the critical Hermite-Gabor exponent

## Finding

For every \(\beta>0\), there are constants \(N_\beta\in\mathbb N\) and \(C_\beta>0\) such that, for every \(n\ge N_\beta\), the conditions
\[
ab\le n^{-2/3}(\log n)^{-\beta}
\]
and
\[
\min\{a,b\}\ge n^{-1/2}(\log n)^{-\beta/2}
\]
imply that
\[
\mathcal G(h_n,a\mathbb Z\times b\mathbb Z)
\]
is a frame for \(L^2(\mathbb R)\).

The statement is quantitatively stronger. If \(S_{n,a,b}\) is the associated frame operator, then
\[
\bigl\|ab\,S_{n,a,b}-I\bigr\|
\le
C_\beta(\log n)^{-\beta/8}
\]
uniformly throughout the displayed region. Hence, for all sufficiently large \(n\), there are frame bounds satisfying
\[
\frac{1-C_\beta(\log n)^{-\beta/8}}{ab}
\le A_{n,a,b}
\le B_{n,a,b}
\le
\frac{1+C_\beta(\log n)^{-\beta/8}}{ab}.
\]

Thus the new near-diagonal safety region reaches the critical product scale \(n^{-2/3}\) up to an arbitrary polylogarithmic loss and is asymptotically tight after the natural normalization by \(ab\).

## Assumptions and scope

The Hermite functions \(h_n\) and the rectangular Gabor system use the normalization of the cited source. The result concerns only the near-diagonal regime
\[
\min\{a,b\}\ge n^{-1/2}(\log n)^{-\beta/2}.
\]
It does not replace the separate near-axis theorem of the source and does not claim a global frame region at product scale \(n^{-2/3}(\log n)^{-\beta}\).

The logarithm is the natural logarithm. Since the theorem is asymptotic, all statements are understood for sufficiently large \(n\).

## Proof

The source proves its near-diagonal theorem for fixed parameters
\[
0<\delta<\eta<\frac13
\]
and the region
\[
\min\{a,b\}\ge n^{-1/2-\delta},
\qquad
ab\le n^{-2/3-\eta}.
\]
The crucial point is that its displayed proof estimates can be run with slowly varying parameters rather than fixed ones.

Fix \(\beta>0\) and define
\[
\eta_n=\beta\frac{\log\log n}{\log n},
\qquad
\delta_n=\frac{\eta_n}{2}.
\]
Then
\[
n^{-\eta_n}=(\log n)^{-\beta},
\qquad
n^{-\delta_n}=(\log n)^{-\beta/2}.
\]
Thus the region in the finding is exactly the source's near-diagonal region with \(\eta=\eta_n\) and \(\delta=\delta_n\).

For the main elliptic-layer decomposition choose
\[
p_n=1-\frac{\eta_n}{4},
\qquad
t_n=\frac23-\frac{\eta_n}{4}.
\]
For large \(n\),
\[
0<t_n<\frac23,
\qquad
\frac13<p_n<1,
\]
and
\[
p_n+t_n
=
\frac53-\frac{\eta_n}{2}
>
\frac53-2(\eta_n-\delta_n)
=
\frac53-\eta_n.
\]
Hence the source's partition parameters satisfy the required inequalities.

We now track the source's displayed estimate for the four non-delicate layers. Its bound becomes
\[
J_1
\le
C\left(
n^{t_n/2-1/3}
+
n^{-(p_n+t_n)/2+5/6+\delta_n-\eta_n}
+
n^{-1/6-\eta_n/2}
+
n^{\delta_n-\eta_n}
\right).
\]
The four exponents simplify to
\[
-\frac{\eta_n}{8},
\qquad
-\frac{\eta_n}{4},
\qquad
-\frac16-\frac{\eta_n}{2},
\qquad
-\frac{\eta_n}{2}.
\]
Therefore
\[
J_1
=
O_\beta\!\left((\log n)^{-\beta/8}\right).
\]

For the delicate dyadic layer, the source decomposes the estimate into three sums. Under the same substitution,
\[
\Sigma_1
\le
4n^{p_n/2-2/3-\eta_n}
=
4n^{-1/6-9\eta_n/8},
\]
\[
\Sigma_2
\le
4n^{-\eta_n/2}
=
4(\log n)^{-\beta/2},
\]
and
\[
\Sigma_3
\le
Cn^{-1/6+\delta_n-\eta_n}\log n
=
Cn^{-1/6}(\log n)^{1-\beta/2}.
\]
Each is
\[
O_\beta\!\left((\log n)^{-\beta/8}\right).
\]

It remains to verify that the large-\(X\) tail estimate survives the drifting parameters. In the source proof the tail parameter is
\[
\varepsilon_n
=
\frac23-2(\eta_n-\delta_n)
=
\frac23-\eta_n.
\]
The explicit tail bound only needs
\[
\pi n^{-\varepsilon_n}<0.1
\]
and
\[
\exp\!\left(-\frac{\pi}{4}n^{1-\varepsilon_n}\right)<\frac12
\]
for large \(n\). Here
\[
n^{-\varepsilon_n}
=
n^{-2/3}(\log n)^\beta\longrightarrow0
\]
and
\[
n^{1-\varepsilon_n}
=
n^{1/3}(\log n)^\beta\longrightarrow\infty.
\]
Consequently the source's exponential tail bound remains valid and is much smaller than every negative power of \(\log n\).

Combining the finite-layer and tail estimates gives
\[
\sup
\sum_{(k,l)\ne(0,0)}
\left|
V_{h_n}h_n\left(\frac{k}{b},\frac{l}{a}\right)
\right|
=
O_\beta\!\left((\log n)^{-\beta/8}\right),
\]
where the supremum is over the region in the finding.

Finally, Janssen's representation gives
\[
ab\,S_{n,a,b}
=
I+
\sum_{(k,l)\ne(0,0)}
c_{k,l}\,
\pi\!\left(\frac{k}{b},\frac{l}{a}\right),
\]
with
\[
|c_{k,l}|
=
\left|
V_{h_n}h_n\left(\frac{k}{b},\frac{l}{a}\right)
\right|.
\]
Since every time-frequency shift is unitary,
\[
\bigl\|ab\,S_{n,a,b}-I\bigr\|
\le
\sum_{(k,l)\ne(0,0)}|c_{k,l}|
\le
C_\beta(\log n)^{-\beta/8}.
\]
For large \(n\) the right side is less than one, which proves the frame property and the stated frame-bound estimates.

## Verification

The proof uses no numerical experiment.

The critical parameter identities were checked algebraically:
\[
t_n/2-1/3=-\eta_n/8,
\]
\[
-(p_n+t_n)/2+5/6+\delta_n-\eta_n=-\eta_n/4,
\]
\[
p_n/2-2/3-\eta_n=-1/6-9\eta_n/8,
\]
and
\[
-1/6+\delta_n-\eta_n=-1/6-\eta_n/2.
\]

The source's tail argument was checked at the level of its explicit displayed estimate rather than by invoking its fixed-parameter proposition as a black box. The two conditions used to obtain the final exponential tail bound remain valid because
\[
n^{-2/3}(\log n)^\beta\to0
\]
and
\[
n^{1/3}(\log n)^\beta\to\infty.
\]

The frame-operator conclusion follows from the standard Janssen representation and the triangle inequality in operator norm.

## Relationship to prior work

Faulhuber, Shafkulovska, and Zlotnikov prove that, for every fixed \(\eta>0\), the full product region
\[
ab\le n^{-2/3-\eta}
\]
eventually lies in the Hermite frame set after combining a near-diagonal argument with a separate near-axis theorem. Their near-diagonal proof assumes fixed
\[
0<\delta<\eta<1/3.
\]
The theorem stated here is not a formal consequence of that result: taking \(\eta=\eta_n\to0\) inside a theorem whose threshold depends on \(\eta\) gives no quantitative conclusion. The new argument reopens the explicit estimates and shows that the proof remains valid for the drifting logarithmic parameters.

The same source records that the exponent \(1/2\) governing the near-axis transition is asymptotically sharp because of known non-frame points. The present statement does not challenge that obstruction; it stays on the near-diagonal side of that scale.

The 2025 frame-set paper of the same authors enlarges the classical safety region at specific square lattices and through finite-dimensional estimates, but does not provide the present asymptotic logarithmic window. The 2025 non-frame paper of Horst, Lemvig, and Videbæk constructs obstructions on fixed rational-density hyperbolas, with one lattice parameter of order \(n^{1/2}\) and the other of order \(n^{-1/2}\); those obstructions concern the axis regime rather than the logarithmic near-diagonal strip above.

## Limitations

The result is confined to
\[
\min\{a,b\}\ge n^{-1/2}(\log n)^{-\beta/2}.
\]
It does not prove that every lattice with
\[
ab\le n^{-2/3}(\log n)^{-\beta}
\]
is a frame.

The exponent \(\beta/8\) in the operator-norm error is the rate furnished by the tracked source estimates. It is not claimed to be optimal.

The theorem reaches the power exponent \(2/3\) only with a logarithmic loss. It does not settle whether a fixed positive constant times \(n^{-2/3}\) is a universal near-diagonal safety threshold.

## References

1. M. Faulhuber, I. Shafkulovska, and I. Zlotnikov, *Asymptotic safety regions for Gabor frames generated by Hermite functions*, arXiv:2609.01296v1, 2026.
2. M. Faulhuber, I. Shafkulovska, and I. Zlotnikov, *On the Frame Property of Hermite Functions and Exploration of their Frame Sets*, Journal of Fourier Analysis and Applications 31 (2025), Article 21.
3. A. Horst, J. Lemvig, and A. E. Videbæk, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, Applied and Computational Harmonic Analysis 76 (2025), 101747; arXiv:2311.01547.
