# Coadjoint-rank strata and central commutator fibers in the four-by-four triangular algebra

## Finding
Let \(q\) be any prime power, \(T=T_4(\mathbb F_q)\) the ten-dimensional associative algebra of upper triangular four-by-four matrices, and \(\mathfrak n=[T,T]\) its six-dimensional strictly upper triangular ideal. Index the natural basis of \(\mathfrak n\) as \((E_{12},E_{13},E_{14},E_{23},E_{24},E_{34})\). For \(\lambda=(a,b,c,d,e,f)\in\mathfrak n^*\), put \(B_\lambda(X,Y)=\lambda(XY-YX)\) and \(r(\lambda)=\operatorname{rank}B_\lambda\). All five possible ranks and their complete multiplicities are:

| Rank | Number of functionals |
| --- | --- |
| \(0\) | \(1\) |
| \(2\) | \(3(q-1)\) |
| \(4\) | \(2q^2(q-1)+3(q-1)^2\) |
| \(6\) | \(3q^2(q-1)^2+(q-1)^3+(q-1)q^4\) |
| \(8\) | \(q^2(q-1)^3+(q-1)^2q^4\) |

Moreover, for every \(h\in\mathbb F_q\) define the prescribed additive-commutator fiber
\[
F_q(h)=\big|\{(X,Y)\in T^2:XY-YX=hE_{14}\}\big|.
\]
Then
\[
F_q(0)=q^8(q^2+q-1)(q^4+5q^3-3q^2-4q+2)
\]
and, for every \(h\ne0\),
\[
F_q(h)=q^8(q-1)(q+1)(q^2+q-1)(q^2+4q-2).
\]
In particular, the exact zero-versus-nonzero highest-root fiber gap is
\[
F_q(0)-F_q(h)=q^{11}(q^2+q-1)>0\qquad(h\ne0).
\]
These assertions hold uniformly in all characteristics, including characteristic two.

## Assumptions and scope
The brackets here are **additive associative-algebra commutators** \([X,Y]=XY-YX\), not multiplicative commutators in the triangular matrix group. All ten triangular entries of each input matrix are unrestricted. The functional \(\lambda\) is extended from \(\mathfrak n\) to \(T\) by assigning zero on diagonal matrix units. For arbitrary \(q\), the rank of the alternating matrix \(B_\lambda\) is even. The target \(hE_{14}\) is central within the strictly upper triangular Lie ideal but not central in the full triangular Lie algebra; the terminology "highest-root target" therefore denotes its root position, not centrality in \(T\). No assertion is made for arbitrary six-coordinate targets or larger matrix sizes.

## Proof
Use the basis \((E_{11},E_{12},E_{13},E_{14},E_{22},E_{23},E_{24},E_{33},E_{34},E_{44})\) of \(T\). Since
\[
[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj},
\]
the skew matrix \(B_\lambda\) is determined by these displayed structure constants, with any diagonal root coordinate interpreted as zero. Write
\[
\Delta=be-cd,\qquad Q=ae+bf.
\]
All size-eight principal Pfaffians, up to signs and repetitions, are exactly the six polynomials
\[
\Delta c^2,\quad \Delta ac,\quad\Delta bc,\quad\Delta ce,\quad\Delta cf,\quad\Delta Q.
\]
The symbolic computation is reproduced independently in `artifacts/check_pfaffians.py`; because a skew matrix has rank at least eight exactly when some size-eight principal Pfaffian is nonzero, this identifies the rank-eight locus over **every** field, rather than just at tested primes. The same explicit Pfaffians furnish the rank-six witnesses \(c^3\), \(b^2e\), \(b^2f\), and \(ae^2\), while the size-four Pfaffians include \(b^2\) and \(e^2\).

A complete disjoint rank analysis follows, valid also in characteristic two:

* If \(c\ne0\), the size-six witness \(c^3\) is nonzero, and rank eight occurs exactly when \(\Delta\ne0\); otherwise rank six occurs.
* If \(c=0\) and \(be\ne0\), the size-six witness \(b^2e\) is nonzero. Rank eight occurs exactly when \(Q\ne0\), and rank six otherwise.
* If \(c=e=0\) and \(b\ne0\), rank six occurs exactly when \(f\ne0\), by the witness \(b^2f\) and the vanishing of all size-eight Pfaffians. When \(f=0\), the form is supported entirely on the upper-left three-by-three triangular subalgebra: its rank is exactly four, as follows from the nonzero size-four Pfaffian \(b^2\) and direct elimination of the six-dimensional triangular block.
* If \(c=b=0\) and \(e\ne0\), the transposed-reversal analogue has rank six exactly when \(a\ne0\), and otherwise rank four.
* If \(b=c=e=0\), the root-root block vanishes, and the diagonal-root incidence block has rank equal to the number of nonzero entries among \(a,d,f\). Thus the full skew matrix has twice that rank.

These cases give the five multiplicities in the theorem by counting free variables. For example, when \(c\ne0\), exactly \((q-1)q^4\) functionals have \(\Delta=0\), and exactly \((q-1)^2q^4\) have \(\Delta\ne0\). With \(c=0\), the rank-eight count is \(q^2(q-1)^3\); rank six has \(3q^2(q-1)^2+(q-1)^3\); rank four has \(2q^2(q-1)+3(q-1)^2\); rank two has \(3(q-1)\); and rank zero has one. Their sum, including the \(c\ne0\) contributions, is exactly \(q^6\).

Let \(\psi:\mathbb F_q\to\mathbb C^\times\) be a nontrivial additive character. Orthogonality gives the standard finite-field bilinear Fourier identity
\[
F_q(h)=q^{14}\sum_{\lambda\in\mathfrak n^*}q^{-r(\lambda)}\psi(-ch).
\]
Indeed, fixing \(\lambda\), the sum of \(\psi(\lambda([X,Y]))\) over the two ten-dimensional arguments equals \(q^{20-r(\lambda)}\); division by \(|\mathfrak n|=q^6\) imposes the six commutator equations.

Let \(A(q)\) be the weighted sum of \(q^{-r}\) over \(c=0\), and \(B(q)\) the corresponding sum over \(c\ne0\). From the rank strata,
\[
\begin{aligned}
A(q)&=1+\frac{3(q-1)}{q^2}+\frac{2q^2(q-1)+3(q-1)^2}{q^4}\\
&\quad+\frac{3q^2(q-1)^2+(q-1)^3}{q^6}+\frac{q^2(q-1)^3}{q^8},\\
B(q)&=\frac{q-1}{q^2}+\frac{(q-1)^2}{q^4}.
\end{aligned}
\]
For each fixed nonzero \(c\), its weighted contribution is \(B(q)/(q-1)\), independently of \(c\). Therefore \(F_q(0)=q^{14}(A+B)\), while for \(h\ne0\), the identity \(\sum_{c\ne0}\psi(-ch)=-1\) gives \(F_q(h)=q^{14}(A-B/(q-1))\). Elementary polynomial expansion yields the displayed factorizations and gap.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and no third-party dependencies. It constructs the bracket matrix independently from matrix-unit multiplication, exhaustively evaluates its ranks over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), checks the complete rank table, and solves **every** prescribed commutator linear system over \(\mathbb F_2\) to confirm the two special fibers, obtaining \(48640\) and \(38400\). It also checks the symbolic central-fiber factorizations at eight field-size inputs. Run `python3 artifacts/check_pfaffians.py` with SymPy installed to reproduce the exact polynomial size-eight Pfaffian set and the crucial lower-order witnesses. Both checks were executed successfully. The symbolic Pfaffian identity and the argument above, not the finite-field samples, support the all-prime-power assertion.

## Relationship to prior work
Kostant (2012) proves maximal coadjoint orbit **codimensions** for complex Borel Lie algebras by using strongly orthogonal roots. For the four-by-four triangular Lie algebra, the maximal rank eight is consistent with that structural theory. His theorems do not supply the complete finite-field stratified rank multiplicities or prescribed highest-root additive-commutator fibers established here. Kaur, Sharma and Singh (2020) study **group** conjugacy branching matrices and commuting probabilities of invertible triangular and unitriangular matrices, not all-element additive Lie-algebra commutator fibers. Work on additive triangular three-by-three fibers concerns a smaller Lie algebra and does not imply the rank-eight degeneration \(\Delta Q=0\) present here. These comparisons concern mathematical implication, not merely title differences.

## Limitations
This is a complete Kirillov-form rank distribution but only a two-case formula for **highest-root targets** of the additive commutator map. Other target fibers are not classified. It does not determine orbit counts or group commutator distributions. A prior detailed finite-field coadjoint classification of four-by-four Borel algebras, perhaps phrased via orbit representatives instead of ranks, could imply parts of these formulas; historical priority has not been exhaustively resolved. All checks are self-review; no independent mathematical audit has been performed.

## References
1. Bertram Kostant, *Coadjoint structure of Borel subgroups and their nilradicals*, arXiv:1205.2362v1 (first submitted 2012-05-10), Sections 1–2, https://arxiv.org/abs/1205.2362.
2. Dilpreet Kaur, Uday Bhaskar Sharma, and Anupam Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1 (first submitted 2020-06-02), Sections 4, 6, 8, https://arxiv.org/abs/2006.01493.
3. V. Dergachev and A. Kirillov, *Index of Lie algebras of seaweed type*, Journal of Lie Theory 10 (2000), 331–343; background for generic Lie-algebra index methods, not claimed to settle the finite-field distribution.
