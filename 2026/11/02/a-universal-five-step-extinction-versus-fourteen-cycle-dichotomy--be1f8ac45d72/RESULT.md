# A universal five-step extinction versus fourteen-cycle dichotomy from one incidence toggle

## Finding

Let \(\Pi\) be **any** finite projective plane of even order \(q\ge 2\), including a plane that is not Desarguesian. Put \(v=q^2+q+1\), write \(B\in\mathbb F_2^{v\times v}\) for its point-by-line incidence matrix and \(\rho=\operatorname{rank}_{\mathbb F_2}B\). For one point \(p\) and one line \(\ell\), toggle their incidence in the Levi graph: delete that edge if \(p\in\ell\), or insert it if \(p\notin\ell\). On the resulting \(2v\)-vertex graph apply synchronous binary open-neighborhood XOR at every vertex, with global linear map \(F\).

**Deleted incidence.** Every initial state reaches zero in at most five updates; the bound is attained. The exact iterate-rank profile is
\[
\big(\operatorname{rank}F^0,\ldots,\operatorname{rank}F^5\big)
=(2v,\,2\rho+2,\,6,\,4,\,2,\,0).
\]
The zero state is the unique recurrent state. If \(E_t\) counts states whose *first* zero is at time \(t\), then \(E_0=1\) and, for each \(1\le t\le5\),
\[
E_t=2^{2v-\operatorname{rank}F^t}-2^{2v-\operatorname{rank}F^{t-1}}.
\]

**Inserted nonincidence.** The exact iterate ranks are
\[
\operatorname{rank}F^0=2v,\qquad
\operatorname{rank}F^1=2\rho+2,\qquad
\operatorname{rank}F^t=6\quad(t\ge2).
\]
The \(64\) states in \(\operatorname{im}F^2\) are precisely the recurrent states. They form exactly **one fixed state, one primitive seven-cycle, and four primitive fourteen-cycles**. Every state enters its eventual cycle within two updates, and this bound is sharp; in particular \(F^{16}=F^2\), whereas \(F^9\ne F^2\).

For addition the exact first-cycle-entry counts are
\[
E_0=64,\quad E_1=2^{2v-2\rho+4}-64,\quad
E_2=2^{2v}-2^{2v-2\rho+4}.
\]
Every periodic state has exactly \(2^{2v-6}\) states in its eventual phase fiber; hence the fixed orbit has basin size \(2^{2v-6}\), the unique seven-cycle has basin \(7\cdot2^{2v-6}\), and each of the four fourteen-cycles has basin \(14\cdot2^{2v-6}\). No other orbit periods or first-entry times occur. In **both** edited graphs the modified incidence matrix has binary rank \(\rho+1\).

The core phenomenon is independent of the projective-plane isomorphism type and of the edited point-line pair. The \(2\)-rank \(\rho\), which may encode the geometry of the plane, affects transient *populations* but not the period list or the sharp maximal entrance time.

## Assumptions and scope

A finite projective plane of order \(q\) has \(v=q^2+q+1\) points, as many lines, exactly \(q+1\) points per line and lines per point, and a unique common line through any two distinct points (dually, a unique intersection point of distinct lines). Assume \(q\) is even and \(q\ge2\). No coordinate field, geometric automorphism transitivity, regularity of the edited graph, or prime-power representation is required. The state space is the \(\mathbb F_2\)-vector space \(\mathbb F_2^{2v}\), with the vertex order points followed by lines. Time is discrete and starts at \(0\). Eventual-cycle entry means the least \(t\ge0\) such that \(F^t(x)\) is periodic.

Write \(u\in\mathbb F_2^v\) for the all-ones column vector; \(J=uu^{\mathsf T}\). Fix coordinate columns \(e=e_p\) and \(f=e_\ell\); let \(b=Bf\) and \(c=B^{\mathsf T}e\), and set \(\delta=e^{\mathsf T}b\). Thus \(\delta=1\) for a deletion and \(\delta=0\) for an insertion. Define
\[
C=B+ef^{\mathsf T},\qquad
A=\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix};
\]
then \(F(x)=Ax\). All matrices, ranks, products, traces of iterations, and powers below are over \(\mathbb F_2\).

## Proof

**1. Incidence parity and rank boost.** For even \(q\), both \(q+1\) and \(v\) are odd. The projective-plane axioms give
\[
BB^{\mathsf T}=B^{\mathsf T}B=J,\quad
Bu=B^{\mathsf T}u=u,\quad
u^{\mathsf T}u=1,
\quad u^{\mathsf T}b=b^{\mathsf T}b=1.
\]
The vectors \(u,b,e\) are linearly independent: \(u\) has weight \(v\), \(b\) has weight \(q+1\), \(e\) has weight \(1\), and \(b+e\) cannot be \(u\) or zero for \(q\ge2\); the same holds for \(u,c,f\). Moreover, \(e\notin\operatorname{im}B\): otherwise \(e=By\) would imply \(c=B^{\mathsf T}e=Jy\), a constant column, contrary to the incidence row \(c\), which has both zeros and ones. Dually \(f\notin\operatorname{im}B^{\mathsf T}\). The latter assertion ensures a vector \(z\in\ker B\) with \(f^{\mathsf T}z=1\), so \(Cz=e\). Therefore \(\operatorname{im}B\subseteq\operatorname{im}C\), since \(By=Cy+e(f^{\mathsf T}y)\). As \(e\notin\operatorname{im}B\), and a single rank-one perturbation changes rank by at most one, \(\operatorname{rank}C=\rho+1\). Consequently \(\operatorname{rank}A=2\rho+2\). Any three distinct incidence rows of \(B\) are linearly independent: otherwise their sum would be zero and its dot product with any fourth distinct row would be \(1+1+1=1\), a contradiction. Thus \(\rho\ge3\).

**2. A universal three-dimensional image.** Expand
\[
P=CC^{\mathsf T}=J+be^{\mathsf T}+eb^{\mathsf T}+ee^{\mathsf T},
\qquad Q=C^{\mathsf T}C=J+cf^{\mathsf T}+fc^{\mathsf T}+ff^{\mathsf T}.
\]
The three independent coefficient functionals \(u^{\mathsf T}\), \(e^{\mathsf T}\), and \((b+e)^{\mathsf T}\) show \(\operatorname{im}P=U:=\operatorname{span}(u,b,e)\) and \(\operatorname{rank}P=3\). Dually \(\operatorname{im}Q=U':=\operatorname{span}(u,c,f)\) and \(\operatorname{rank}Q=3\). Since \(A^2=P\oplus Q\), this proves \(\operatorname{rank}A^2=6\) in both cases. The basis actions are, using \(\delta=e^{\mathsf T}b\),
\[
Pu=u+b,\qquad
Pb=u+\delta b+(1+\delta)e,\qquad
Pe=u+b+(1+\delta)e.
\]
The same equations, with \(b,e\) replaced by \(c,f\), hold for \(Q\) on \(U'\).

**3. Deletion.** If \(\delta=1\), all three basis vectors map under \(P\) to \(w=u+b\), and under \(Q\) to \(w'=u+c\). Since \(Pw=P(u+b)=0\), direct substitution gives
\[
P^2=ww^{\mathsf T}\ne0,\quad Q^2=w'w'^{\mathsf T}\ne0,
\qquad P^3=Q^3=0.
\]
Also
\[
C^{\mathsf T}u=u+f,\qquad
C^{\mathsf T}b=u+\delta f=u+f,
\]
so \(C^{\mathsf T}w=0\); dually \(Cw'=0\). Thus \(A^4=P^2\oplus Q^2\) has rank two, and \(A^5=0\). To identify the third rank, note that \(C^{\mathsf T}|_U\) has rank two: the independent nonzero images are \(u+f\) and \(C^{\mathsf T}e=c+f\). Its dual analogue \(C|_{U'}\) also has rank two. As \(\operatorname{im}P=U\) and \(\operatorname{im}Q=U'\), \(\operatorname{rank}A^3=4\). The displayed rank profile and extinction counts follow by rank-nullity; \(A^4\ne0\) makes five steps sharp.

**4. Insertion.** If \(\delta=0\), then on \(U\), in the ordered basis \((u,b,e)\), the matrix of \(P\) is
\[
M=\begin{pmatrix}1&1&1\\1&0&1\\0&1&1\end{pmatrix},
\qquad \chi_M(t)=t^3+t+1.
\]
This cubic is irreducible over \(\mathbb F_2\), hence its nonzero roots have multiplicative order seven. In particular \(M^7=I\), and \(M^j-I\) is invertible for \(1\le j<7\). The identical statements hold for \(Q|_{U'}\). The six-dimensional \(W=U\oplus U'=\operatorname{im}A^2\) is therefore \(A\)-invariant; \(A|_W\) is invertible and \((A|_W)^{14}=I\). Since \(A^2\) has image \(W\), every state enters \(W\) by time two and \(A^{16}=A^2\). The rank of \(A\) exceeds six because \(\rho\ge3\), so some state does not enter the periodic space after only one update; the two-step maximum is attained.

On \(W\), \(A^2\) has order seven and no nonzero fixed vector. Consequently, \(A\) has only possible primitive periods \(1,7,14\) there (period two is ruled out). The only fixed state is zero. The seventh power \(A^7\) exchanges \(U\) and \(U'\), with each interchanged block an isomorphism because \(A|_W\) is invertible. Therefore \(\dim\ker(A^7-I)|_W=3\): choose an arbitrary state in one three-dimensional part, and the other part is uniquely determined. Of its eight fixed states, one is zero and the other seven form one primitive seven-cycle. The remaining \(64-8=56\) states form four primitive fourteen-cycles. This also shows \(A^9\ne A^2\).

Finally, linear primary decomposition applies directly: \(V=\ker A^2\oplus W\) because \(A^2\) is invertible on \(W\). For \(t=0,1,2\), first-entry layers are obtained from the nested subspaces \(W\subseteq\ker A+W\subseteq V\); their dimensions are \(6\), \(6+\dim\ker A=2v-2\rho+4\), and \(2v\). This gives the first-entry counts. The map \(A^2:V\to W\) is surjective with kernel of size \(2^{2v-6}\). Two states enter the same phase of a periodic orbit if and only if their two-step images agree, so every periodic state has a phase fiber of precisely that size; summing over each cycle gives the basin formulas.

## Verification

The standalone `verify_planes.py` constructs \(\mathrm{PG}(2,2)\), \(\mathrm{PG}(2,4)\), and \(\mathrm{PG}(2,8)\) over binary finite fields, confirms their point-line incidence axioms, and checks the full predicted rank profiles for one incident and one nonincident edited pair. The associated binary incidence ranks are \(4\), \(10\), and \(28\), respectively. Its independent full-state run on the Fano plane checks all \(2^{14}=16{,}384\) configurations for each edit type, including first-entry times, orbit periods, and all basin sizes.

The separate `verify_fano_all_edits.py` uses a cyclic difference-set model of the Fano plane and ordinary Boolean-array elimination, rather than the first program's finite-field and bitset implementations. It checks **all 49** possible toggles: 21 deletions and 28 additions, including each claimed matrix identity and its relevant fixed-space dimensions. Actual output is embedded in the accompanying text artifacts. These finite checks support, but do not replace, the all-projective-planes proof above.

## Relationship to prior work

Noual, Regnault and Sené (first arXiv posting 2012-08-14, `arxiv:1208.2767`) study synchronous XOR dynamics and convergence times, especially **circulant** interaction matrices; its Section 4.2 gives exact convergence theorems for two-neighbor power-of-two circulant networks. Those systems are not incidence graphs of projective planes, nor do those results imply the asymmetric single-incidence-toggle classification given here. The standard projective-plane identity \(BB^{\mathsf T}=qI+J\) and general finite-field linear-map decompositions are known tools, not claimed as discoveries. De Winter, Lazebnik and Verstraëte (2008) study the projective-plane incidence graph for extremal graph cycles, not XOR dynamics.

The present result concerns a different graph family and the precise effect of either kind of *one-edge* mutation: a nilpotency index of five versus a six-state-dimensional periodic component of order fourteen. Dedicated literature searches found no directly equivalent prior statement, but this is not a proof of first discovery; equivalent historical finite-geometry or binary-matrix calculations could exist outside the inspected material.

## Limitations

Only even-order projective planes are treated. The proof does not assume that planes exist for every even integer; it is conditional on a plane's existence. The incidence \(2\)-rank \(\rho\) is left as a legitimate plane-dependent parameter rather than claimed to have one universal formula. The claim does not include weighted automata, asynchronous updates, or multi-edge perturbations. Independent mathematical review has not been performed. Historical priority is not certified by database search.

## References

1. M. Noual, D. Regnault, S. Sené, *Boolean networks synchronism sensitivity and XOR circulant networks convergence time*, arXiv:1208.2767, first posted 2012-08-14, especially Section 4. [https://arxiv.org/abs/1208.2767](https://arxiv.org/abs/1208.2767).
2. S. De Winter, F. Lazebnik, J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics 15 (2008), #R143. [https://doi.org/10.37236/867](https://doi.org/10.37236/867).
3. R. A. Hernández Toledo, *Linear finite dynamical systems*, Communications in Algebra 33 (2005). General finite linear-map background; not a source for the special incidence-toggle calculations.
