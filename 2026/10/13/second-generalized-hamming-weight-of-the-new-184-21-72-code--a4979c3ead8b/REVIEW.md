# Self-review

## Correctness
PASS. For any binary two-dimensional subcode \(D=\langle u,v\rangle\), every coordinate in \(\operatorname{Supp}(D)\) occurs in exactly two of \(u,v,u+v\), hence
\[
2|\operatorname{Supp}(D)|=\operatorname{wt}(u)+\operatorname{wt}(v)+\operatorname{wt}(u+v)\ge216.
\]
The published code was reconstructed from its explicit quasi-cyclic specification. Exhaustive enumeration of all \(2^{21}\) messages recovers minimum distance \(72\) and \(9{,}826\) minimum words. The messages \(0x63\), \(0x318\), and \(0x37b\) give three weight-\(72\) words spanning support \(108\). Exhaustive testing of all \(48{,}270{,}225\) unordered pairs in the minimum shell gives \(1{,}748{,}433\) additive pairs, or exactly \(582{,}811\) minimizing two-spaces.

## Originality
PASS. The closest source is the manuscript that introduces the explicit code: it states its parameters, gives its quasi-cyclic construction, and reports \(A_{72}=9826\), but the inspected full text does not state \(d_2\) or count additive triples among minimum words. Searches using the code parameters, the source identifier, generalized-Hamming terminology, union-support language, and minimum-shell additive-triple language found no result implying the finalized claim. Previously compared same-code hull and coordinate-incidence data do not determine pairwise closure of the minimum shell.

Residual risk: an unindexed supplementary computation could independently contain the same higher-weight invariant.

## Value
PASS. The result fixes the first higher support invariant of a newly reported record code and shows it attains the sharp binary lower bound \(d_2\ge3d_1/2\). The exact count of \(582{,}811\) minimizing two-spaces further records substantial additive structure in the minimum shell, a feature not visible in the ordinary weight enumerator or coordinate-incidence spectrum.

Self-review: passed. Independent audit: not yet performed.
