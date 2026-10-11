# Review of the finite-field paraboloid coordinate Fourier frame

## Correctness: PASS

For every odd prime-power order \(q\), the proof fixes the normalized surface measure and lists all \(3q-2\) chosen characters. The complete square identity gives the exact nonconstant cross-terms \(s\psi(-a^2/(4c))\), and the partial Fourier matrix satisfies \(H\mathbf1=-\mathbf1\) and \(HH^*=qI-J\). These identities split the Hermitian Gram into \(3(q-1)/2\) trivial unit directions, \((q-3)/2\) coupled two-dimensional blocks, a \((q-3)/2\)-dimensional kernel space, and a residual four-dimensional Hermitian block. Their dimensions sum to \(3q-2\). The symbolic determinant check proves the isolated cubic. Its discriminant and the explicit resultant separate all positive eigenlevels; the boundary substitutions give nullity exactly one at \(q=3,5\), otherwise none. The asymptotics follow from Vieta and the polynomial evaluated at \(q-1\). See `RESULT.md` and reproducible `symbolic_certificate.py` and `paraboloid_frame_check.py`.

## Originality: PASS, with historical-equivalence risk

Mockenhaupt--Tao (arXiv:math/0204234) analyze finite-field restriction/Kakeya, and Iosevich--Koh (arXiv:0805.0814) derive paraboloid Fourier surface-measure identities and extension estimates. Those contain mathematical input to this proof but their inspected main statements do not determine this particular coefficient Gram spectrum or the two congruence-class conditioning laws. Casazza--Fickus (DOI:10.1155/ASP/2006/70204) develop correlations for finite cyclic chirps; the object, restricted frequency family, and all-field spectrum differ. Iosevich--Koh (arXiv:0804.4505) study restriction on nondegenerate quadratic level surfaces rather than this paraboloid coordinate-character frame. Published-result searches for quadratic graph frame spectra, aliases via chirp Gram matrices, and finite-field restriction, plus comparisons with mathematical claims, did not reveal a theorem implying the seven-level multiset. These checks are not a claim of exhaustive global novelty: an older equivalent frame or association-scheme specialization could exist.

## Value: PASS

The coordinate-frequency family is the simplest joint linear/quadratic Fourier measurement family on the canonical finite-field paraboloid, so its exact coefficient conditioning is a natural invariant. The result determines the full spectrum, every equality space, and the two exceptional dependencies, while revealing the different asymptotic behavior for the two congruence classes. This goes beyond re-deriving Gauss sums or finite numerical examples, and supplies sharp quantitative information for a complete infinite family of restrictions.

## Closest literature and limitations

The original paraboloid restriction and paraboloid Fourier-transform papers contain needed ingredients but address different operator inequalities. Related quadratic-chirp frame identities may potentially give the same result after a nonobvious reduction; independent priority and verification have not been obtained. The theorem excludes arbitrary mixed Fourier frequencies, all even-characteristic fields, and general quadrics. The symbolic and numerical checkers are supplemental to the self-contained proof.

Same-model review: passed. Independent audit: not yet performed.
