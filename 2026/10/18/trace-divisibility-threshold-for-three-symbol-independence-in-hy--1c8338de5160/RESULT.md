# Trace-divisibility threshold for three-symbol independence in hyperbolic toral maps

## Finding
Let \(t\ge3\) and \(q\ge2\) be integers. On \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), let \(T_t(z)=A_tz\pmod{\mathbb Z^2}\), where
\[
A_t=\begin{pmatrix}t&-1\\1&0\end{pmatrix}.
\]
Initialize \(Z\) according to normalized Haar measure and set \(x_n=(T_t^nZ)_1\pmod1\), represented in \([0,1)\). For the vertical equal-width observation, define \(C_n=\lfloor qx_n\rfloor\in\{0,\ldots,q-1\}\).

Every two observations at distinct times are independent and uniform. For three consecutive observations, define the probability vector \(w_{t,q}\) on residues \(r\in\{0,\ldots,q-1\}\) by
\[
w_{t,q}(r)=\frac1{2t}\left[\mathbf1_{r\equiv-1\ ({\rm mod}\ q)}+\mathbf1_{r\equiv t-1\ ({\rm mod}\ q)}+2\sum_{j=0}^{t-2}\mathbf1_{r\equiv j\ ({\rm mod}\ q)}\right].
\]
Then the complete three-symbol cylinder law, for every \(i,j,k\in\{0,\ldots,q-1\}\), is
\[
\boxed{\mathbb P(C_0=i,C_1=j,C_2=k)=\frac1{q^2}w_{t,q}((k-tj+i)\bmod q).}
\]
Thus three consecutive symbols are jointly independent **if and only if**
\[
\boxed{q=2\quad\text{or}\quad q\mid t.}
\]
More strongly, if \(q=2\), observations at **any three distinct nonnegative times** are jointly independent fair binary symbols.

Writing \(H(w)=-\sum_{r:w(r)>0}w(r)\log w(r)\), with natural logarithms, the exact conditional mutual information of the first and third observations given the middle one is
\[
\boxed{I(C_0;C_2\mid C_1)=\log q-H(w_{t,q}).}
\]
It is zero precisely in the independence cases above. Once the sensor resolves at least \(t+1\) bins, its defect is the **exact** log-resolution law
\[
\boxed{I(C_0;C_2\mid C_1)=\log(q/t)-\frac{\log2}{t},\qquad q\ge t+1.}
\]

## Assumptions and scope
All assertions concern the deterministic, invertible, hyperbolic toral automorphism above under normalized Haar initial measure; no noise, quantization of the phase-space dynamics, or Markov coding is imposed. The observations are non-generating vertical strip symbols, rather than the stable/unstable-oriented rectangles of a Markov partition. Boundary conventions affect zero-Haar-measure sets only. The integer trace restriction \(t\ge3\) makes the two eigenvalues positive reciprocal real numbers off the unit circle, and \(q\ge2\) is an arbitrary integer sensor alphabet size. The three-symbol law applies to consecutive times; the all-time triple-independence claim is made only for the binary alphabet.

## Proof
**1. Haar pairs.** Since \(A_t\in SL(2,\mathbb Z)\), normalized Haar measure is invariant. The first coordinate rows \(v_n=e_1^{\mathsf T}A_t^n\) satisfy
\[
v_{n+2}=t v_{n+1}-v_n.
\]
For any \(m>n\), the integer linear map \(z\mapsto(v_nz,v_mz)\pmod1\) has determinant equal in absolute value to \(a_{m-n}\), where \(a_0=0\), \(a_1=1\), and \(a_{h+1}=t a_h-a_{h-1}\). By induction, \(0<a_h<a_{h+1}\) for every \(h\ge1\) when \(t\ge3\); thus this map is a surjective finite covering of \(\mathbb T^2\). It pushes Haar measure to Haar measure. Consequently \(x_n,x_m\) are independent uniform circle coordinates; their equal-bin labels are independent uniform symbols.

**2. Exact three-symbol law.** The map \(z\mapsto(x_0,x_1)\) is a toral automorphism (its integral row matrix has determinant \(-1\)), so the pair is independent uniform. Conditional on \(C_0=i,C_1=j\), write
\[
x_0=\frac{i+U}{q},\qquad x_1=\frac{j+V}{q},
\]
where \(U,V\) are independent uniform on \([0,1)\). The Cayley–Hamilton recurrence gives \(x_2=tx_1-x_0\pmod1\), hence
\[
C_2\equiv tj-i+\lfloor tV-U\rfloor\pmod q.
\]
Direct integration of the strip \(r\le tV-U<r+1\) in the unit square gives
\[
\mathbb P(\lfloor tV-U\rfloor=r)=
\begin{cases}
1/(2t),&r=-1\text{ or }r=t-1,\\
1/t,&0\le r\le t-2,\\
0,&\text{otherwise}.
\end{cases}
\]
For example, the lower end triangle has area \(\int_0^{1/t}(1-tv)\,dv=1/(2t)\); translating the integral over successive unit strips gives the interior values, and reflection of the square gives the upper endpoint. Reduction modulo \(q\) proves the boxed cylinder law.

**3. Sharp independence criterion.** A probability vector on \(\mathbb Z/q\mathbb Z\) is uniform exactly when all its nontrivial discrete Fourier coefficients vanish. The generating Laurent polynomial of the preceding strip law is
\[
P_t(z)=\sum_{r=-1}^{t-1}\mathbb P(\lfloor tV-U\rfloor=r)z^r
=\frac{1+z^{-1}}{2t}\sum_{j=0}^{t-1}z^j.
\]
For a nontrivial \(q\)-th root of unity \(z\), this vanishes whenever \(z=-1\) or \(z^t=1\). If \(q=2\), the only nontrivial root is \(-1\), so uniformity holds. If \(q\ge3\), choose a primitive \(q\)-th root: it is not \(-1\), so its coefficient vanishes only if \(q\mid t\). Conversely, if \(q\mid t\), every nontrivial \(q\)-th root satisfies \(z^t=1\), so every nontrivial coefficient vanishes. This proves the if-and-only-if statement without extrapolation from finite experiments.

**4. All distinct binary triples.** At \(q=2\), define \(S_n=1-2C_n\in\{\pm1\}\). Every single sign has zero mean and any two distinct signs have zero product expectation by Step 1. Under the Haar-preserving inversion \(Z\mapsto-Z\), each \(S_n\) changes sign outside a null set. The product of any three distinct signs therefore has expectation zero. Fourier–Walsh inversion of the law of three signs shows that all eight outcomes have probability \(1/8\), proving joint independence for arbitrary distinct times.

**5. Exact information loss.** By Step 1, \(H(C_2\mid C_1)=\log q\). Conditional on \(C_0,C_1\), Step 2 gives a cyclic translate of \(w_{t,q}\), so \(H(C_2\mid C_0,C_1)=H(w_{t,q})\). Their difference is the claimed conditional mutual information. It vanishes precisely when \(w_{t,q}\) is uniform, already classified in Step 3. If \(q\ge t+1\), the \(t+1\) residues \(-1,0,\ldots,t-1\) are distinct modulo \(q\). Consequently \(w_{t,q}\) consists of two positive masses \(1/(2t)\), \(t-1\) masses \(1/t\), and zeros elsewhere; direct entropy summation yields \(H(w_{t,q})=\log t+(\log2)/t\), proving the last formula.

## Verification
The accompanying standalone `check.py` uses exact rational polygon clipping and the shoelace formula to integrate each region \(r\le tV-U<r+1\) for every integer \(3\le t\le30\). It compares these areas with the claimed weights, checks the modular uniformity criterion for \(2\le q\le40\), checks the high-resolution entropy identity numerically, and verifies nonvanishing integer row determinants for the first nine times over \(3\le t\le20\). Running `python check.py` reports `VERIFY_OK`. The proof above, not these bounded checks, establishes all statements for every allowed \(t,q\) and arbitrary distinct binary observation times.

## Relationship to prior work
The hyperbolic toral automorphism framework and the symbolic coding by stable/unstable-oriented Markov rectangles are classical. Siemaszko and Wojtkowski (2010) classify two-rectangle Berg partitions of hyperbolic toral automorphisms; the classification is about partitions with sides along stable/unstable eigendirections and does not furnish the present equal-width coordinate-strip cylinder law. Bakker and Rodrigues (2011) study algebraic and profinite conjugacy invariants using periodic data, not the Haar distribution of finite-resolution observations. The present statement does not claim the matrix family, Haar invariance, or Fourier methods to be new. Its specific contribution is the complete three-block distribution for coordinate-strip quantization, the sharp divisibility criterion, the all-time binary triple property, and the exact conditional-information law.

## Limitations
These observations are not Markov rectangles and the theorem does not identify a finite-order Markov process or an entropy rate for arbitrary-length label sequences. In the \(q\ge3\) case, the independence characterization applies to consecutive triples, not arbitrary triples. No result is asserted for arbitrary non-Haar invariant measures, for noninteger traces, or for perturbations of the automorphism. The historical originality comparison is limited to inspected publications and targeted searches; a pre-existing calculation of the same coordinate-strip cylinders would take priority. No independent audit has been conducted.

## References
- A. Siemaszko and M. P. Wojtkowski, *Counting Berg partitions*, first public preprint 22 July 2010, arXiv:1007.3984, especially Sections 1, 4–5.
- L. F. Bakker and P. Martins Rodrigues, *A Profinite Group Invariant for Hyperbolic Toral Automorphisms*, first public preprint 4 February 2011, arXiv:1102.0839, especially Sections 1, 3 and 6.
