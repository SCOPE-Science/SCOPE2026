# Same-model scientific review: binary \(4\times4\) Fourier optimizer classification

## Correctness — PASS
The statement has fixed finite quantifiers: all 65,536 sign arrays supported on the full square; normalized Haar fourth moment; explicitly defined aperiodic displacements; and explicitly defined symmetry group. Fourier orthogonality yields \(M=256+2\sum_{\mathcal H}C^2\); a different Parseval convolution formula is independently checked on every one of 8192 sign-normalized inputs. The eightfold reduction is proved free using three designated signs. The actual packaged `checker.py` reproduces four normalized minimizers, 32 original minimizers, two disjoint 16-element symmetry orbits, and each representative's large-shift geometry. The finite enumeration is complete for the stated finite domain; it is not an argument about all other sizes or continuous phases.

## Originality — PASS with explicit residual risk
The sharp numerical bound is **known**, as Schmidt's arXiv:1105.5176, p. 2, attributes \(F_{4,4}=16/3\) to Eggers's 1986 Table 4.2; there is no new-best-value claim. The final mathematical claim concerns the complete two-orbit classification, the exact count 32, and the orthogonal/oblique dominant-lobe dichotomy. The examined full texts of Schmidt, Svalbe–Tirkel (2017), and Pai–Chen (2021) do not state or imply that classification: they respectively concern scalar/asymptotic merit factors, periodic array families, and complementary sets. Semantic and alias searches of published mathematical result records did not return an equivalent claim. However, the original 1986 Eggers dissertation and the full 1993 Bömer–Antweiler paper were not materially examined; a class list in either remains possible. A failed search is not a novelty certificate.

## Value — PASS
A complete optimizer space of a canonical fully populated planar Fourier aperture is a natural finite classification. Two inequivalent minimizer shapes with the same best total sidelobe energy but different orientations of their two maximal sidelobes provide information that a sharp scalar value or a single example cannot supply. This distinction is useful as a precise finite benchmark for array correlation construction and directional constraints, without alleging unproved practical performance gains. The result is more than a routine numerical increment: it resolves the exact symmetry geometry of all equality cases for this shape.

## Closest literature and limits
Schmidt (arXiv:1105.5176), Eggers (1986, dissertation Table 4.2 cited secondhand), Bömer–Antweiler (Signal Processing 30, 1993), Svalbe–Tirkel (doi:10.1186/s13634-017-0455-2), and Pai–Chen (arXiv:2102.04043) were compared by implication, not title. Full-text gaps for Eggers and Bömer–Antweiler remain a genuine priority risk. Complete coverage is claimed only for binary \(4\times4\) arrays and the stated group.

Same-model review: passed. Independent audit: not yet performed.
