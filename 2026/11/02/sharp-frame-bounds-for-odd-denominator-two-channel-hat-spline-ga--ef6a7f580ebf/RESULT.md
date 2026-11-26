# Sharp frame bounds for odd-denominator two-channel hat-spline Gabor lattices

## Finding

For every odd integer \(q\ge3\), let \(g(t)=(1-|t|)_+\), \(a=2/q\), and \(M_k f(t)=e^{2\pi i kt}f(t)\), \(T_xf(t)=f(t-x)\). The system \(\{M_k T_{ja}g:j,k\in\mathbb Z\}\) is a frame, with optimal squared-analysis constants
\[
A_q=\frac{q^2-1}{6q},\qquad B_q=\frac{2q^2+1+\sqrt{(q^2-1)^2+9}}{6q}.
\]
That is, the sum of squared frame coefficients is bounded below and above by these multiples of \(\|f\|_2^2\). The frame-operator condition number is
\[
\kappa_q=2+\frac{3}{q^2-1}+\sqrt{1+\frac{9}{(q^2-1)^2}}.
\]
It decreases strictly to \(3\), with maximum \((19+\sqrt{73})/8\) at \(q=3\). At \(q=3\), the bounds are \(4/9\) and \((19+\sqrt{73})/18\).

## Proof

Work with the translated hat \(G=T_1g\), supported on \([0,2]\) with branches \(t\) and \(2-t\). The systems for \(G\) and for \(g\) are related by the unitary \(T_1\), which commutes with all integer modulations \(M_k\) and all time translations. **The coefficient formulas below use \(G\), not the centered hat \(g\).**

Parseval in the integer modulation variable gives, first on compactly supported functions, the frame operator
\[
(Sf)(t)=D(t)f(t)+E(t)f(t-1)+E(t+1)f(t+1),\quad
D(t)=\sum_j G(t-ja)^2,\quad E(t)=\sum_j G(t-ja)G(t-ja-1).
\]
Indeed, periodizing \(f(t)\overline{G(t-ja)}\) with unit period computes its integer Fourier coefficients; the resulting products of shifted windows vanish for shifts of magnitude at least two. The finitely many terms at each \(t\) are bounded uniformly in \(t\), so the identity extends by boundedness. The coefficients are \(a\)-periodic and \(E\ge0\).

Write \(f\) unitarily as \((f(t+n))_{n\in\mathbb Z}\) for \(0\le t<1\). Since \(2=qa\), each fiber has period two in \(n\). Fourier series in the even and odd cell index gives the Hermitian matrix
\[
H(t,\varphi)=\begin{pmatrix}
D(t)&E(t+1)+e^{-i\varphi}E(t)\\
E(t+1)+e^{i\varphi}E(t)&D(t+1)
\end{pmatrix},\qquad 0\le\varphi<2\pi.
\]
A shift of \(t\) by \(1/q\) interchanges \(D(t),D(t+1)\) and \(E(t),E(t+1)\), since \(q\) is odd. The trace and the squared modulus of the off-diagonal entry, hence the eigenvalues, are unchanged. Thus it suffices to consider \(0\le t\le1/q\). The larger eigenvalue is maximized in phase, and the smaller eigenvalue minimized, at \(\varphi=0\): the triangle inequality gives the largest off-diagonal modulus there.

Put \(q=2m+1\) and \(z=qt\). At \(t\) the \(q\) arguments of \(G\) in \([0,2]\) are \((z+2j)/q\), \(0\le j<q\), up to zero endpoints; at \(t+1\) use \((z+2j+1)/q\) by periodicity. On the first group the rising branch has \(m+1\) samples and the falling branch \(m\); on the second group the numbers are exchanged (at endpoints either convention gives the same values). At \(z=0\) the first sum of squares is \(8\sum_{j=1}^{m}j^2/q^2=(q^2-1)/(3q)\); the first sum has zero slope at zero by reflection and its quadratic coefficient in \(z\) is \(q/q^2\). Reflection combined with a shift by \(a\) maps the second diagonal sum to the first evaluated at \(1-z\). Therefore
\[
D(t)=\frac{q^2-1+3z^2}{3q},\qquad D(t+1)=\frac{q^2-1+3(z-1)^2}{3q}.
\]
The product sum on either group has terms \((u-1)(2-u)\) for \(1\le u\le2\). At the endpoints the products sum to \(q^{-2}\sum_{r=1,3,\ldots,2m-1} r(q-r)=(q^2-1)/(12q)\); replacing odd by even \(r\) gives the same sum by \(r\mapsto q-r\). The interior quadratic coefficients in \(z\) are \(-m/q^2\) and \(-(m+1)/q^2\), respectively, by the branch counts. Hence
\[
E(t)=\frac{q^2-1}{12q}+\frac{m z(1-z)}{q^2},\qquad E(t+1)=\frac{q^2-1}{12q}+\frac{(m+1)z(1-z)}{q^2}.
\]
In particular, if working with the original centered window, the two coefficient values in each pair must instead be interchanged.

Set \(w=(2z-1)^2\). The trace, diagonal difference, and off-diagonal sum are \((4q^2-1+3w)/(6q)\), \((2z-1)/q\), and \((2q^2+1-3w)/(12q)\) respectively. At phase zero the eigenvalues are
\[
\lambda_\pm(w)=\frac{4q^2-1+3w\pm R(w)}{12q},\qquad
R(w)=\sqrt{(2q^2+1-3w)^2+36w}.
\]
Each is strictly increasing on \([0,1]\): the derivative is \((1\pm(5-2q^2+3w)/R(w))/(4q)\) and \(R(w)^2-(5-2q^2+3w)^2=24(q^2-1)>0\). The minimum of the smaller is \(\lambda_-(0)=A_q>0\), and the maximum of the larger is \(\lambda_+(1)=B_q\). Continuity gives these same essential extrema even though the extremizing fibers have measure zero. This proves the frame bounds and their optimality. Division gives \(\kappa_q\), whose terms after the constant \(2\) strictly decrease and sum to \(1\) in the limit.

## Verification and scope

\(q\) must be odd, with unit modulation spacing; the argument does not cover other rational numerators or other windows. The finite `CHECK.py` script uses exact arithmetic for the sample sums of the translated hat and numerical checks for the direct Zak-fiber reconstruction of the centered hat. These finite checks supplement, rather than replace, the exact all-\(q\) argument.

## Relationship to prior work

The Walnut and Zibulski–Zeevi representations supply the operator framework. The contribution is the explicit optimization of both spectral edges for the stated family, not a claim that rational fiberization or qualitative coverage of the lattice family is new. Stangl and Frederick's integer-oversampled result in arXiv:2609.00481 does not address these bounds. Atindehou, Frederick, Kouagou and Okoudjou analyze the spline frame set and dual constructions in arXiv:1806.05614. The Resultary record *Uniform quantitative frames on the odd-denominator two-channel tori* (08edf77a8415) gives valid, not necessarily optimal, bounds at the same density for the fixed hat with \(b=5/2\), not \(b=1\). Dilation changing \(b\) also dilates the window and does not identify the two fixed-hat systems. No absolute priority is claimed.
