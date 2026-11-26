# Independent mathematical audit

## correctness

PASS

With e=e* and w_±=(1±e)^(1-2/k), the supplied definitions simplify to V1=(1-e^2)(w_-+w_+)/2 and e V2=(1-e^2)(w_--w_+)/2: multiply the inverse powers by (1-e^2) to obtain (1+e)w_- and (1-e)w_+, then cancel e V1. V1 is strictly positive. Normalizing the derived timing equation transcribed in RESULT.md by 2pi/T_r leaves e V2/V1 multiplying sin(chi). At k=1, w_±=1/(1±e), giving V1=V2=1. At k=2, w_±=1, giving V1=1-e^2 and V2=0. The corrected law therefore gives nt=chi at the exact harmonic limit stated in the derivation as reported, while the inversion paper's reported reciprocal is undefined for every 0<e<1 there. This check is algebraic, with no general exact-timing or inversion-error claim. The primary wording and equation locators were not independently retrieved; the textual comparison rests on the precise transcriptions and matching definitions in the frozen package.

## originality

PASS

Limited to the explicit correction of the inversion paper's reported reciprocal and its consequence for using that formula in harmonic timing. The correct approximate timing law, its coefficient, and the exact harmonic limit are credited to the earlier derivation as reported in the frozen record. The distinction is the identification of an inconsistency in the other paper, not a new central-orbit timing result. The bounded comparison did not establish a prior explicit correction of the inversion formula; primary pagination and possible unindexed errata remain unresolved.

## value

PASS

This is a usable correction to the input coefficient of a general inversion procedure, not just a normalization preference. For every admissible nonzero harmonic eccentricity the reported reciprocal causes division by zero where inversion is exactly linear. For fixed eccentricity near k=2 the corrected coefficient tends to zero and has absolute value below one, while the reported reciprocal grows without bound and can destroy monotonicity of the displayed timing map. Ordinary Kepler-case validation cannot detect the error. That failure mode makes the narrowly scoped correction worth documenting, without implying a new theory or a general error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
