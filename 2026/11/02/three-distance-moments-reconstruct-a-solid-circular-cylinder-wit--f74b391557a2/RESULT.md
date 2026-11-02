# Three distance moments reconstruct a solid circular cylinder, with an exact two-moment fold

## Finding

Let \(C_{R,H}=\{(x,y,z)\in\mathbb R^3:x^2+y^2\le R^2,\ 0\le z\le H\}\), with arbitrary \(R>0\), \(H>0\). Let \(X,Y\) be independent, uniformly volume-distributed points of \(C_{R,H}\), let \(D=\|X-Y\|_2\), and write \(m_j=\mathbb E[D^{2j}]\), \(j=1,2,3\).

**Theorem (sharp three-moment cylinder tomography).** The triple \((m_1,m_2,m_3)\) uniquely determines both \(R\) and \(H\). More precisely, setting \(s=m_1\), the exact positive reconstruction is
\[
\begin{aligned}
Q&=4371m_2-5912s^2\ge433s^2>0,\\
v&=\frac{\frac{13454}{3}m_3-s(19529m_2-16852s^2)}{Q},\\
R&=\sqrt{s-v},\qquad H=\sqrt{6v}.
\end{aligned}
\]
For data from a nondegenerate cylinder these radicals have strictly positive arguments.

**The exact two-moment ambiguity.** Given \(s>0\), a pair \((m_1,m_2)=(s,M)\) arises from a nondegenerate right circular cylinder if and only if
\[
\frac{45}{31}\le\frac{M}{s^2}<\frac{12}{5}.
\]
It determines precisely two noncongruent cylinders if and only if
\[
\frac{45}{31}<\frac{M}{s^2}<\frac53,
\]
and precisely one cylinder otherwise. The two candidates in the ambiguous range are characterized by distinct positive \(v,v'\) satisfying \(v+v'=20s/31\). Their sixth-distance moments have the **exact resolving separation**
\[
|m_3(v)-m_3(v')|=\frac{3Q}{13454}|v-v'|
\ge\frac{1299}{13454}s^2|v-v'|.
\]
The universal coefficient in the last inequality cannot be increased: the ratio approaches equality as the two candidates coalesce at \(v=v'=10s/31\). Thus **three moments are necessary and sufficient globally**.

## Assumptions and scope

The cylinder is a *filled* Euclidean right circular cylinder, not merely its lateral surface. The two points are independent and sampled according to normalized three-dimensional volume. Both radius and height are strictly positive, with no restriction on their ratio. The power moments are exact population moments; numerical data can incur estimation errors not bounded by this theorem. Congruence is understood in Euclidean space, so rigid motion and reflection are immaterial.

The parameters \(u=R^2\) and \(v=H^2/6\) both have the units of squared length. In particular \(s=u+v>0\). The moment order \(m_j\) means \(\mathbb E[D^{2j}]\), so the three observations are the second, fourth, and sixth powers of distance.

## Proof

**1. Independent radial and axial contributions.** Write the sampled points as \(X=(U,Z_1)\), \(Y=(V,Z_2)\) where \(U,V\) are independent uniform points in the planar radius-\(R\) disk and \(Z_1,Z_2\) are independent uniforms on \([0,H]\). Set \(T=\|U-V\|_2^2\) and \(B=(Z_1-Z_2)^2\). Then \(D^2=T+B\) and \(T,B\) are independent.

For the planar disk, squared polar radii are independent and uniform on \([0,R^2]\), and the relative angle is uniform on \([0,2\pi)\). Expanding \(T=A_1+A_2-2\sqrt{A_1A_2}\cos\Theta\), and using \(\mathbb E[\cos\Theta]=\mathbb E[\cos^3\Theta]=0\) and \(\mathbb E[\cos^2\Theta]=1/2\), gives
\[
\mathbb E[T]=u,\qquad
\mathbb E[T^2]=\frac53u^2,\qquad
\mathbb E[T^3]=\frac72u^3.
\]
For the axial interval, \(Z_1-Z_2\) has triangular density, whence for every nonnegative integer \(j\),
\[
\mathbb E[B^j]=\frac{2H^{2j}}{(2j+1)(2j+2)}.
\]
In particular \(\mathbb E[B]=v\), \(\mathbb E[B^2]=12v^2/5\), and \(\mathbb E[B^3]=54v^3/7\).

**2. Exact moment polynomials.** Binomial expansion of \((T+B)^j\) yields
\[
\begin{aligned}
m_1&=u+v=s,\\
m_2&=\frac53u^2+2uv+\frac{12}{5}v^2
=\frac53s^2-\frac43sv+\frac{31}{15}v^2,\\
m_3&=\frac72u^3+5u^2v+\frac{36}{5}uv^2+\frac{54}{7}v^3\\
&=\frac72s^3-\frac{11}{2}s^2v+\frac{77}{10}sv^2+\frac{141}{70}v^3.
\end{aligned}
\]
These are exact rational identities for every \(u,v>0\), not empirical approximations.

**3. The two-moment fold and exact feasible region.** At fixed \(s\), \(0<v<s\). The quadratic \(m_2(v)\) has its unique minimum \(45s^2/31\) at \(v_*=10s/31\), takes the excluded endpoint value \(5s^2/3\) at \(v=0\), and approaches the excluded maximal endpoint \(12s^2/5\) as \(v\uparrow s\). Consequently the image of \(0<v<s\) is exactly \([45s^2/31,12s^2/5)\).

For two inputs to the quadratic to give the same \(m_2\), their values either agree or satisfy \(v+v'=20s/31\). Both distinct candidates lie in \((0,s)\) exactly when \(0<v,v'<20s/31\), equivalent to \(45s^2/31<m_2<5s^2/3\). This proves the complete multiplicity classification. For example, \(s=1\) and \(v=8/31\) or \(v'=12/31\) produce distinct cylinders \((R^2,H^2)=(23/31,48/31)\) and \((19/31,72/31)\), both with \(m_2=679/465\), whereas their respective sixth moments are \(5480483/2085370\) and \(5508719/2085370\). Hence two moments do not suffice.

**4. Algebraic elimination and separation.** Direct substitution of the quadratic expression for \(m_2\) into the cubic expression for \(m_3\), followed by polynomial collection, establishes the exact identity
\[
m_3=\frac3{13454}\left[s(19529m_2-16852s^2)+v(4371m_2-5912s^2)\right].
\]
Completing the square in \(m_2\) gives
\[
4371m_2-5912s^2\ge
\left(\frac{4371\cdot45}{31}-5912\right)s^2=433s^2>0.
\]
The displayed inverse expression therefore isolates \(v\) uniquely and recovers \(R,H>0\). On a fixed two-moment fiber \((s,m_2)\), subtracting the last identity at \(v,v'\) gives the exact sixth-moment separation and the bound stated in the theorem. The coefficient is sharp because \(v\ne v'\) can approach \(10s/31\) from opposite sides, when \(Q/s^2\to433\). This finishes the proof.

## Verification

The accompanying standalone `verification.py` symbolically checks the three moment polynomial expressions, the cubic-to-quadratic elimination identity, the positive denominator minimum, and the exact rational two-cylinder witness. It also independently generates two uniform points directly in three different cylinders using seeded numerical simulation and compares the observed second, fourth, and sixth moments against the analytic expressions. The package-specific replay produced `ALL_CHECKS_PASSED`. The algebraic proof above, not the simulations, establishes the universal assertions.

## Relationship to prior work

Kellerer (1981) derived the **forward** point-pair distance distribution of general right cylinders, including circular cylinders, by convolving horizontal and vertical separations; the forward convolution and cylinder-distance probability law are expressly prior work, not claimed here. In particular the elementary product decomposition in Step 1 is consistent with that framework. The present finding addresses the distinct **inverse finite-data problem**: the sharp number of even distance moments sufficient to identify the cylinder, the exact one-/two-valued moment map, a closed rational inverse, and a sharp sixth-moment branch separation.

Bäsel (2021) treats random-point distance moments for regular planar polygons and their circular-disk limit; this provides independent planar moment background but does not supply the three-dimensional cylinder inverse. Pure et al. (2019) treat planar-polygon point-distance distributions. Neither their planar geometry nor Kellerer's forward map, as read, states the finite cylinder inverse classification. The moment formulas are computable from earlier forward theory; historical priority for the specific inverse theorem has not been independently established.

## Limitations

The inverse assumes exact observations and strictly positive parameters. It does not give optimal statistical sample sizes or global noisy-data error bounds for estimated moments, although the denominator is uniformly positive relative to scale. It does not extend by itself to noncircular, hollow, oblique, or capped cylinders. The sharp separation bound compares two candidates **having identical first two moments**; it is not an estimate between arbitrary pairs of cylinders. The prior-work search cannot exclude an older formulation of the finite inverse theorem; no claim of exhaustive historical novelty or independent certification is made.

## References

1. A. M. Kellerer, *Proximity Functions for General Right Cylinders*, Radiation Research **86** (1981), 264–276. Lawfully accessible full article: https://epub.ub.uni-muenchen.de/8544/1/8544.pdf (especially Eq. (14), Eq. (16), and Appendix).
2. U. Bäsel, *The moments of the distance between two random points in a regular polygon*, first public arXiv version January 11, 2021, arXiv:2101.03815, https://arxiv.org/abs/2101.03815 (circular-disk limit included).
3. R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, first public March 18, 2019, arXiv:1903.07757, https://arxiv.org/abs/1903.07757.
