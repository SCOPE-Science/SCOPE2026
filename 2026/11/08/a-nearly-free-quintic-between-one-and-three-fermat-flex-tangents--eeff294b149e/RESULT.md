# A nearly free quintic between one and three Fermat flex tangents

## Finding
Let \(\omega\in\mathbb C\) satisfy \(\omega^2+\omega+1=0\), with \(\omega\ne1\). Set \(E=V(x^3+y^3+z^3)\subset\mathbb P^2_{\mathbb C}\), and let \(L_j=V(x+\omega^j y)\) for \(j=0,1,2\). For any distinct \(i,j\in\{0,1,2\}\), the reduced quintic \(D_{ij}=E\cup L_i\cup L_j\) is **nearly free with exponents \((2,3)\)**. Its complete singularity basket is \(2A_5+A_1\), its total Tjurina number is \(11\), and its minimal Jacobian-syzygy degree is \(2\). The degree-four curve obtained by adding only one of these lines is not nearly free; adjoining all three lines gives the already-known free sextic with exponents \((2,3)\). The new assertion is the two-line near-free stage, not the published three-line freeness statement.

## Assumptions and scope
Work over \(\mathbb C\), in homogeneous coordinates \([x:y:z]\). A plane curve of degree \(d\) is called nearly free when the minimal degree \(r\) of a nonzero homogeneous Jacobian syzygy satisfies \(r<d/2\) and the total Tjurina number is \((d-1)^2-r(d-r-1)-1\); its exponents are then \((r,d-r)\). We use the equivalent criterion recalled in Dimca--Ilardi--Pokora--Sticlaru (2023), Definition 3.5. A flex line to a smooth cubic is a line meeting it with local intersection multiplicity three. A closed point of type \(A_m\) has local analytic equation \(u^2+v^{m+1}=0\). The claim is about embedded reduced arrangements over the complex numbers, not characteristic-positive reductions or the freeness of arbitrary added tangents.

## Proof
The three linear factors \(x+y\), \(x+\omega y\), and \(x+\omega^2 y\) multiply to \(x^3+y^3\). Each \(L_j\) meets \(E\) only at \([1:-\omega^{-j}:0]\), with multiplicity three: substituting \(x=-\omega^j y\) makes the cubic equal \(z^3\). Thus the corresponding union has a local equation with two smooth branches meeting to order three, analytically \(A_5\). The lines \(L_i,L_j\) meet transversely at \([0:0:1]\), which is not on \(E\); hence there is one further node \(A_1\) and no other singularity. The local singularities are quasihomogeneous, so their Tjurina numbers are their Milnor numbers, and \(\tau(D_{ij})=5+5+1=11\).

All unordered pairs are equivalent under the projective transformations \([x:y:z]\mapsto[\omega^k x:y:z]\) and the interchange of \(x,y\), so it suffices to analyze \(F=(x^3+y^3+z^3)(x+y)(x+\omega y)\). Define quadratic forms
\[
A=x^2+(1+\omega)xy-5\omega y^2,\qquad
B=5\omega x^2+xy+(1+\omega)y^2,\qquad
D=z(x+(1+\omega)y).
\]
Direct expansion using \(\omega^2+\omega+1=0\) gives the nontrivial Jacobian relation \(AF_x+BF_y+DF_z=0\). Thus \(\operatorname{mdr}(F)\le2\).

For the reverse inequality, form the \(21\times9\) coefficient matrix of the nine homogeneous degree-five forms \(xF_x,yF_x,zF_x,xF_y,yF_y,zF_y,xF_z,yF_z,zF_z\). Its reduction modulo seven under \(\omega\mapsto2\) has column rank nine by exact row reduction; the attached checker supplies all entries and verifies the rank. Since a nonzero minor after reduction is already nonzero in \(\mathbb Z[\omega]\), the matrix has full column rank in characteristic zero. Therefore no degree-one Jacobian syzygy exists. A degree-zero syzygy would yield a degree-one syzygy after multiplication by a variable, so \(\operatorname{mdr}(F)=2\).

With \(d=5\) and \(r=2\), the nearly free numerical criterion reads \((5-1)^2-2(5-2-1)-1=11\), exactly the Tjurina total above. Thus \(D_{ij}\) is nearly free with exponents \((2,3)\). The single-tangent quartic has only one \(A_5\) singularity, so \(\tau=5\); the numerical near-free criterion gives \(\tau=6\) for the possible minimal syzygy degrees \(1\) or \(2\), hence it is not nearly free. For all three lines the free-sextic assertion is Dimca et al., Corollary 1.6 (2023), not a new result.

## Verification
Run \(`python verify_flex_quintic.py`\) with Python 3 and SymPy installed. The program verifies the displayed Jacobian relation in the integral extension \(\mathbb Z[\omega]\), proves that the nine linear-syzygy columns have rank nine by reduction modulo seven, checks the standard near-free numerical identity, and emits \(`FLEX_QUINTIC_VERIFY_OK`\). The geometric \(A_5\) and \(A_1\) classifications follow from the explicit local intersection multiplicities in the proof; no numerical finite-field sampling is used in place of a characteristic-zero proof.

## Relationship to prior work
Dimca, Ilardi, Pokora and Sticlaru construct free curves by adjoining **all** inflectional tangent lines associated with the complete set of binary factors; in this example they identify the free degree-six union of the Fermat cubic and all three concurrent flex lines. They also discuss a larger near-free degree-nine union formed by two complete flex triples, not the degree-five two-line subarrangement. Their Definition 3.5 gives the numerical criterion used here. The novelty asserted is the exact intermediate degree-five near-free stage and the one/two/three addition boundary. General near-free-curve definitions and addition--deletion methods are established background, not new claims.

## Limitations
The assertion classifies only the subsets of the particular three concurrent Fermat flex tangents. It does not classify all arrangements of two lines and a smooth cubic, nor all nearly free quintics. A published equivalent result expressed via more general addition--deletion machinery may exist; originality is assessed against inspected texts and accessible records, not independently certified. No independent mathematical audit has been performed.

## References
- A. Dimca, G. Ilardi, P. Pokora and G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v1 (first public January 3, 2023); expanded v4, October 8, 2023. Relevant: Theorem 1.5, Corollary 1.6, Definition 3.5, and Section 5.
- G. Malara, P. Pokora and H. Tutaj-Gasińska, *On 3-syzygy and unexpected plane curves*, Geometriae Dedicata 214 (2021), 49--63. Background on nearly free curves.
- A. du Plessis and C. T. C. Wall, *Application of the theory of the discriminant to highly singular plane curves*, Math. Proc. Camb. Phil. Soc. 126 (1999), 259--266. Numerical Tjurina bound used through the first reference.
