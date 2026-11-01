# Exact coordinate correlations and a singular relaxation crossover in a random identity–doubling map

## Finding
Consider the random interval map \(X_{n+1}=T_{\xi_n}(X_n)\), with independent choices \(\Pr(\xi_n=1)=a\) and \(\Pr(\xi_n=2)=1-a\). The maps on \([0,1)\) are
\[
T_1(x)=\begin{cases}x,&0\le x<1/2,\\2x-1,&1/2\le x<1,\end{cases}\qquad T_2(x)=2x\bmod1.
\]
For every \(0\le a<1\), initiate the process in its known stationary density
\[
h_a(x)=\begin{cases}2/(2-a),&0\le x<1/2,\\2(1-a)/(2-a),&1/2\le x<1.\end{cases}
\]
Write \(C_n(a)=\mathbb E[X_0X_n]-\mathbb E[X_0]^2\), where expectations include both the starting state and the independent map choices. **For all integers \(n\ge0\)**, the generating function is
\[
\boxed{\sum_{n\ge0}C_n(a)z^n=\frac{N_a(z)}{48(2-a)^2(2-az)[4-(2+3a)z+az^2]}}
\]
with
\[
N_a(z)=(3a^4-22a^3+20a^2)z^2+(-10a^3+132a^2-128a)z+8a^2-128a+128.
\]
The three possible decay factors are \(a/2\) and
\[
\lambda_\pm(a)=\frac{2+3a\pm\sqrt{9a^2-4a+4}}8.
\]
The slow factor obeys \(\lambda_+(a)=1-\tfrac23(1-a)+O((1-a)^2)\). For every fixed \(u>0\) and \(a_n=1-u/n\) (for \(n>u\)),
\[
\boxed{\lim_{n\to\infty}C_n(a_n)=\frac{1}{48}e^{-2u/3}.}
\]
The normalization \(1/48\) is the variance of the uniform distribution on the lower half-interval. The theorem concerns covariance for stationary initial conditions and the annealed (map-averaged) law.

## Assumptions and scope
There is a fresh independent Bernoulli choice at every integer time. The endpoints of the half-open intervals are immaterial for absolutely continuous starting laws. The parameter range for the stationary formula is \(0\le a<1\); at \(a=1\) the lower half is a set of fixed points and stationary measures are nonunique. The crossover statement uses the specified stationary law for every \(a_n<1\). No assertion about quenched correlations or arbitrary observables is made.

## Proof
Let \(\mathcal P_a\) be the averaged Perron–Frobenius operator acting on integrable signed densities. For functions affine on each of \(I_0=[0,1/2)\) and \(I_1=[1/2,1)\), write \(g(x)=c_j+d_jx\) on \(I_j\). For \(y\in I_0\), the inverse images come from the identity branch, the lower doubling branch, and the upper doubling branch:
\[
(\mathcal P_ag)(y)=a g_0(y)+\frac{1-a}{2}g_0(y/2)+\frac12g_1((y+1)/2).
\]
For \(y\in I_1\), omit the identity contribution. Consequently, the four-dimensional space of two-piece affine densities is *exactly invariant*, and in the coordinate order \((c_0,c_1,d_0,d_1)\) its transfer matrix is
\[
M_a=\begin{pmatrix}
(1+a)/2&1/2&0&1/4\\
(1-a)/2&1/2&0&1/4\\
0&0&(1+3a)/4&1/4\\
0&0&(1-a)/4&1/4
\end{pmatrix}.
\]
The stationary density vector is \(h=(2/(2-a),2(1-a)/(2-a),0,0)^\mathsf T\). Set \(v=(0,0,2/(2-a),2(1-a)/(2-a))^\mathsf T\), the vector of the signed density \(x h_a(x)\). Since
\[
\int_0^1 y g(y)\,dy=\left(\tfrac18,\tfrac38,\tfrac1{24},\tfrac7{24}\right) (c_0,c_1,d_0,d_1)^\mathsf T,
\]
one has, **exactly**,
\[
\mathbb E[X_0X_n]=\ell M_a^n v,
\qquad \ell=(1/8,3/8,1/24,7/24),
\qquad \mathbb E[X_0]=\frac{4-3a}{4(2-a)}.
\]
Taking the formal resolvent \(\ell(I-zM_a)^{-1}v\) and subtracting the stationary mean square divided by \(1-z\) yields the displayed rational generating function by matrix elimination. The characteristic polynomial factors as \((t-1)(t-a/2)[t^2-(2+3a)t/4+a/4]\), giving the possible modes. For \(0\le a<1\), the roots satisfy \(0\le \lambda_-(a)<\max\{a/2,\lambda_-(a)\}<\lambda_+(a)<1\), apart from coincident zero roots at \(a=0\); the covariance therefore decays exponentially at each fixed \(a<1\).

For the crossover, as \(a\uparrow1\), \(\lambda_+(a)=1-2(1-a)/3+O((1-a)^2)\), while \(a/2\to1/2\) and \(\lambda_-(a)\to1/4\). The coefficient \(B_+(a)\) of \(\lambda_+(a)^n\) is the residue \(\lim_{z\to1/\lambda_+(a)}(1-\lambda_+(a)z)\sum_{n\ge0}C_n(a)z^n\); direct substitution into the rational formula gives \(B_+(a)\to1/48\). The other two residues stay bounded near \(a=1\). Consequently, with \(a_n=1-u/n\), the two fast modes vanish and the slow mode tends to \((1/48)e^{-2u/3}\), as claimed. For \(a=0\), the expression reduces to \(C_n(0)=2^{-n}/12\), agreeing with deterministic doubling.

## Verification
The accompanying dependency-free `checker.py` constructs \(M_a\) over exact rational numbers, compares its covariance coefficients with those of the claimed rational generating function through finite orders, and verifies exact special cases. These are reproducibility checks, not substitutes for the transfer-operator and matrix-resolvent proof. The proof applies to every real \(a\in[0,1)\) and every integer \(n\ge0\).

## Relationship to prior work
Maldonado and Pérez Otero introduce the random system and discuss existence of absolutely continuous invariant measures. Pérez Otero's open-access 2023 thesis, Section 4.4, writes the two transformations and obtains precisely the piecewise-constant invariant density used here. These known ingredients are not claimed as new. The new statistic is the *all-lag coordinate covariance* and its sharp singular relaxation crossover, based on an affine-density transfer space larger than the already-used constant-density space. An exact matching formula in another source has not been excluded by independent publication-priority review.

## Limitations
This is an annealed, single-observable statement. It does not prove a uniform total-variation mixing rate, an optimal spectral gap on a large function space, or a quenched correlation formula. The borderline map \(a=1\) has nonunique invariant measures; the limiting variance \(1/48\) refers to the stationary measures selected by \(a\uparrow1\). Independent scientific validation remains outstanding.

## References
- C. Maldonado and R. A. Pérez Otero, “Phase transition in piecewise linear random maps in the interval,” *Chaos* **31** (2021), 093112, DOI: 10.1063/5.0051242. Publicly posted 2021-09-14.
- R. A. Pérez Otero, *Invariant densities and phase transition phenomenon in random maps in the interval*, doctoral thesis, IPICYT (2023), Chapter 4, Section 4.4, especially equation (4.5) and invariant density (4.6). Institutional open-access PDF: https://repositorio.ipicyt.edu.mx/bitstream/handle/11627/5859/Tesis%20de%20Ricardo%20%28Invariant%20densities%20and%20phase%20transition%20phenomenon%20in%20random%20maps%20in%20the%20interval%29.pdf?isAllowed=y&sequence=3.
