# Finite-order flatness obstruction for the intermediate log-subharmonic mean inequality

## Statement

Let \(D\subset\mathbb R^n\), \(n\ge 3\), and for a locally integrable function \(f\) define the normalized ball and sphere means
\[
A(f,a,r)=\fint_{B(a,r)}f(x)\,dx,\qquad
M(f,a,r)=\fint_{\partial B(a,r)}f\,d\sigma .
\]

Consider a positive function \(u\) near \(a\in D\), write \(v=\log u\), and assume \(v\) is subharmonic.  Nozomu Mochizuki asked, for
\[
1<p<\frac{n+2}{n},
\]
whether every log-subharmonic function satisfies locally
\[
A(u^p,a,r)\le M(u,a,r)^p. \tag{1}
\]
His 2005 theorem proves this under the nondegeneracy condition \(\Delta u(a)>0\), and his remarks leave the general intermediate case open.

The following finite-jet theorem removes that nondegeneracy condition whenever \(\log u\) is not flat.

**Theorem.** Suppose that \(v\in C^{2m}\) near \(a\), \(\Delta v\ge0\), and \(m\ge1\) is the least positive order for which the Taylor expansion of \(v-v(a)\) has a nonzero homogeneous term \(P_m\). Then for every
\[
0<p<1+\frac{2m}{n}
\]
there exists \(\rho>0\) such that
\[
A(u^p,a,r)<M(u,a,r)^p\qquad(0<r<\rho). \tag{2}
\]

Consequently, for every \(1<p<(n+2)/n\), (1) holds locally at every positive point at which \(\log u\) has finite order of nonconstancy. In particular:

1. every positive real-analytic log-subharmonic function satisfies (1) locally at every point for the full intermediate range \(1<p<(n+2)/n\);
2. if a positive \(C^\infty\) log-subharmonic function fails (1) locally at \(a\) for some \(1<p<(n+2)/n\), then \(\log u-\log u(a)\) is flat to infinite order at \(a\).

The finite-order exponent is sharp at the level of germs: for every \(m\ge1\) and every \(p>1+2m/n\), there is a positive real-analytic log-subharmonic germ of exact order \(m\) for which the reverse strict inequality holds for all sufficiently small radii.

## Proof

Translate \(a\) to \(0\), divide \(u\) by \(u(0)\), and hence assume \(v(0)=0\). Write the Taylor expansion
\[
v(x)=P_m(x)+P_{m+1}(x)+\cdots+P_{2m}(x)+o(|x|^{2m}), \tag{3}
\]
where each \(P_j\) is homogeneous of degree \(j\) and \(P_m\not\equiv0\). Put
\[
\langle Q\rangle=\fint_{S^{n-1}}Q(\theta)\,d\sigma(\theta).
\]
For a homogeneous polynomial \(Q\) of degree \(d\),
\[
\fint_{B(0,r)} Q(x)\,dx
=\frac{n}{n+d}\,r^d\langle Q\rangle, \qquad
\fint_{\partial B(0,r)} Q\,d\sigma
=r^d\langle Q\rangle. \tag{4}
\]

We also need a sign observation. If \(k\) is the first index for which \(\Delta P_k\not\equiv0\), then \(\Delta P_k\ge0\). Indeed, it is the first nonzero homogeneous term in the Taylor expansion of the nonnegative function \(\Delta v\). Integrating
\[
\Delta P_k(r\theta)
=r^{k-2}\bigl(k(k+n-2)P_k(\theta)+\Delta_{S^{n-1}}P_k(\theta)\bigr)
\]
over the sphere gives
\[
k(k+n-2)\langle P_k\rangle
=\langle\Delta P_k\rangle>0, \tag{5}
\]
so \(\langle P_k\rangle>0\). If \(\Delta P_j=0\), then \(P_j\) is harmonic and \(\langle P_j\rangle=0\).

Define
\[
F_p(r)=A(e^{pv},0,r)-M(e^v,0,r)^p.
\]

### Case 1: a nonharmonic Taylor term occurs before degree \(2m\)

Let \(k<2m\) be the first index with \(\Delta P_k\not\equiv0\). The nonlinear terms in the exponential begin at degree \(2m\), while all \(P_j\) with \(j<k\) are harmonic. Using (4) and (5),
\[
F_p(r)
=p\left(\frac{n}{n+k}-1\right)\langle P_k\rangle r^k+o(r^k)
=
-\frac{pk}{n+k}\langle P_k\rangle r^k+o(r^k)<0. \tag{6}
\]
This conclusion in fact holds for every \(p>0\).

### Case 2: all Taylor terms below degree \(2m\) are harmonic

Assume \(\Delta P_j=0\) for \(m\le j<2m\). From (3),
\[
e^{pv}
=
1+p\sum_{j=m}^{2m}P_j+\frac{p^2}{2}P_m^2+o(|x|^{2m}),
\]
and
\[
e^v
=
1+\sum_{j=m}^{2m}P_j+\frac12P_m^2+o(|x|^{2m}).
\]
All spherical means of \(P_j\) with \(j<2m\) vanish. Therefore (4) yields
\[
\begin{aligned}
F_p(r)
={}&r^{2m}\Bigg[
-\frac{2mp}{n+2m}\langle P_{2m}\rangle\\
&\qquad\qquad
+\frac p2\left(\frac{pn}{n+2m}-1\right)
\langle P_m^2\rangle
\Bigg]+o(r^{2m}). \tag{7}
\end{aligned}
\]
Here \(\langle P_m^2\rangle>0\). Moreover \(\langle P_{2m}\rangle\ge0\): if \(\Delta P_{2m}\equiv0\), the mean is zero; otherwise \(\Delta P_{2m}\) is the first nonzero homogeneous term of \(\Delta v\), and the argument leading to (5) applies.

Thus, when \(p<1+2m/n\), the second term in brackets in (7) is strictly negative and the first is nonpositive. Hence \(F_p(r)<0\) for all sufficiently small \(r>0\). This proves (2).

For the sharpness statement, choose any nonzero homogeneous harmonic polynomial \(H_m\) of degree \(m\) and put
\[
u(x)=e^{H_m(x)}.
\]
Then \(\log u=H_m\) is harmonic, hence subharmonic, and (7) reduces to
\[
F_p(r)
=
\frac p2
\left(\frac{pn}{n+2m}-1\right)
\langle H_m^2\rangle r^{2m}
+o(r^{2m}). \tag{8}
\]
For every \(p>1+2m/n\), the coefficient is positive, proving local failure.

Finally, when \(m=1\), formula (7) becomes
\[
F_p(r)
=
-\frac{p\bigl((n+2-np)|\nabla v(0)|^2+2\Delta v(0)\bigr)}
{2n(n+2)}\,r^2+o(r^2),
\]
which agrees with the second-order coefficient used by Mochizuki.

## Relation to prior work

Mochizuki (2005) explicitly identifies \(1<p<(n+2)/n\) as the intermediate open range. For \(C^2\) log-subharmonic \(u\), his theorem proves local validity when \(\Delta u(a)>0\), and his Proposition shows only that the closure of the bad-point set has empty interior.

Ekonen, Kinnunen, Marola and Sbordone (2009), Theorem 2.3(ii), later proved the global inequality
\[
\left(A\!\left(u^{\,n/(n-1)},a,r\right)\right)^{(n-1)/n}
\le M(u,a,r)
\]
for positive log-subharmonic functions. By monotonicity of normalized \(L^p\) means this gives (1) for every \(p\le n/(n-1)\). For \(n\ge3\),
\[
\frac{n}{n-1}<\frac{n+2}{n},
\]
so a nonempty upper part of Mochizuki's intermediate interval remains outside that global theorem. The finite-jet theorem above covers that entire upper part locally at every finite-order point, as well as the lower part.

The proof uses standard Taylor expansion, spherical harmonic mean identities and the same general Pizzetti-type local philosophy already present in the older literature. The claimed contribution is the finite-order threshold and the resulting infinite-flatness obstruction, not those classical ingredients.

## Limitations

- The result is local and assumes \(u>0\) near the point. It does not treat zeros of a log-subharmonic function.
- It does not settle Mochizuki's full \(C^2\) or \(C^\infty\) question. A possible smooth counterexample in the intermediate range is only forced to be infinitely flat in \(\log u\) at a bad positive point.
- The endpoint \(p=1+2m/n\) is not classified by the displayed leading term.
- The originality assessment is to the best of our knowledge. Higher-order Pizzetti expansions are classical, so an equivalent finite-jet statement could exist under different terminology.

## Reproducibility

The proof is symbolic and self-contained. Formula (7) can be checked directly by substituting the Taylor expansion (3) into the two normalized means and using (4). For \(m=1\), it reduces exactly to Mochizuki's second-order coefficient above. For a sharpness check, take \(n=3\), \(m=2\), \(H_2(x)=x_1^2-x_2^2\): the sign change predicted by (8) occurs at \(p=1+4/3=7/3\).

## References

1. N. Mochizuki, “A Class of Subharmonic Functions and Integral Inequalities, III,” *Interdisciplinary Information Sciences* 11 (2005), 117–125.  
   https://www.jstage.jst.go.jp/article/iis/11/2/11_2_117/_article
2. M. Ekonen, J. Kinnunen, N. Marola, C. Sbordone, “On Beckenbach–Radó type integral inequalities,” *Ricerche di Matematica* 58 (2009), 43–61. DOI: 10.1007/s11587-009-0046-0.  
   https://doi.org/10.1007/s11587-009-0046-0
3. D. H. Armitage, M. Goldstein, “Some remarks on mean-values of subharmonic functions,” *Tohoku Mathematical Journal* 38 (1986), 231–243. DOI: 10.2748/tmj/1178228490.  
   https://doi.org/10.2748/tmj/1178228490
