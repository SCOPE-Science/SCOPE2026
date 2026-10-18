# Rigid equality in odd Fourier uncertainty on the cyclic group of order 27

## Finding
Let \(G=\mathbb Z/27\mathbb Z\), \(\zeta=e^{2\pi i/27}\), and \(\widehat f(y)=\sum_{x\in G}f(x)\zeta^{xy}\). For every nonzero complex function \(f\) satisfying \(f(-x)=-f(x)\),
\[
|\operatorname{supp}f|+|\operatorname{supp}\widehat f|\ge12.
\]
Equality occurs for precisely **one projective line** of odd functions. Its generator is \(h(3u)=e^{2\pi i u/3}-e^{-2\pi i u/3}\) for \(u\in\mathbb Z/9\mathbb Z\), and \(h(x)=0\) outside \(3G\). Both supports equal \(\{3,6,12,15,21,24\}\).

## Assumptions and scope
All functions are complex-valued, not necessarily unimodular. The Fourier transform is unnormalized and uses the positive exponential; conjugating the convention does not change the result. Oddness forces zero at the origin and organizes every nonzero support into opposite pairs. Equality is projective, meaning equivalence under nonzero complex scalar multiplication only (not translation).

## Proof
Write the two support sizes as \(2a\) and \(2b\), with \(1\le a,b\le13\). The elementary finite-group uncertainty-product inequality gives \(4ab\ge27\). If \(a+b\le5\), then \(ab\le6\), contradiction. Hence \(a+b\ge6\), yielding the asserted lower bound.

To classify equality, use the \(13\times13\) odd Fourier matrix \(M_{k,j}=\zeta^{kj}-\zeta^{-kj}\), with \(1\le k,j\le13\). For the positive support-pair index sets \(A,B\subseteq\{1,\ldots,13\}\), a nonzero odd function with pair supports contained in \(A\) and \(B\) exists exactly if the rows of \(M\) indexed by the complement of \(B\), restricted to columns \(A\), have rank below \(|A|\). At equality \(|A|+|B|=6\).

The attached deterministic exact finite-field certificate evaluates \(M\) in \(\mathbb F_{109}\), mapping \(\zeta\) to \(81\), which has exact order \(27\) modulo \(109\). For \((|A|,|B|)=(1,5),(2,4),(3,3)\), it exhausts respectively \(13\binom{13}{5}\), \(\binom{13}{2}\binom{13}{4}\), and \(\binom{13}{3}^2\) support pairs. The only rank-deficient reduction is
\[
A=B=\{3,6,12\}
\]
in the \((3,3)\) case. Symmetry of \(M\) also rules out all other pairs for \((4,2),(5,1)\). **Why the reduction proves exclusion:** if a matrix over \(\mathbb Q(\zeta)\) were rank deficient, its relevant algebraic-integer minors would all vanish; their images under \(\mathbb Z[\zeta]\to\mathbb F_{109}\), \(\zeta\mapsto81\), would vanish as well. Therefore full rank modulo \(109\) certifies full rank over the complex numbers. No converse is asserted.

At the unique surviving index sets, the displayed \(h\) has the required supports. Indeed it is a difference of two order-three characters on the nine-element subgroup \(3G\), so the Fourier transform is supported on the two residue classes \(y\equiv\pm3\pmod9\). Thus the six-point support is attained at both ends. The reduced restricted matrix has rank precisely two over \(\mathbb F_{109}\), proving its complex rank is at least two, while \(h\) gives a nontrivial complex kernel. Consequently the complex kernel is exactly one dimensional, as claimed.

## Verification
Run \(`python3 verify.py`\) with Python 3 standard library only. It enumerates all support pairs with \(a+b=6\) up to the transpose symmetry, computes every relevant finite-field rank, and prints the unique deficient pair. All arithmetic is integer arithmetic modulo \(109\). The certificate proves exclusions over \(\mathbb C\), not the existence of any complex kernel; existence is established analytically by \(h\). Reproduce the output in `verify_output.txt`.

## Relationship to prior work
Garcia, Karaali and Katz give broad uncertainty principles for functions with symmetry, including sine transforms, and explain substantial differences between prime and composite settings. The classical product uncertainty inequality supplies the numerical lower bound here; the additional content is the complete rigidity of the equality class at cyclic order \(27\). The present result concerns one cyclic prime cube, not non-prime fields and not the general nonvanishing-minors property. A related cyclic-order-\(25\) case has different equality geometry, and neither assertion implies this classification.

## Limitations
The claim is confined to cyclic order \(27\) and odd functions. It neither proves a prime-cube family theorem nor a quantitative stability estimate. Its exhaustive exclusion step is finite and exact because the ambient group and support classes are finite; modular singularity alone would not establish a complex singularity. The literature review cannot exclude an unpublished or differently indexed equivalent equality classification.

## References
Garcia, S. R., Karaali, G., and Katz, D. J., *An improved uncertainty principle for functions with symmetry*, first public arXiv:1807.07648 (2018-07-19), later Journal of Algebra, doi:10.1016/j.jalgebra.2021.07.017.

Donoho, D. L. and Stark, P. B., *Uncertainty principles and signal recovery*, SIAM J. Appl. Math. 49 (1989), 906–931.
