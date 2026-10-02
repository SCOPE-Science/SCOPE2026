# Independent mathematical audit — SCOPE-20260908-051
Audit date: 2026-09-30 UTC.
Disposition: **passed**.

## Correctness
Status: **PASS**.

Fresh independent exhaustive FWHT enumeration recomputed all 65,536 four-variable Boolean functions and all 256 five-variable rotation-symmetric functions from the eight cyclic input orbits. Every joint nonlinearity/resiliency cell matches the record; n=4 has 896 functions at nonlinearity 6, and the n=5 RSBF slice has maximum nonlinearity 12 with 36 attainers, 18 balanced and 8 of resiliency 1.

## Originality
Status: **PASS**.

The 2008 Stănică-Maitra paper already reports several notable five-variable RSBF extrema, including eight (5,1,3,12) functions, but the checked text did not state the complete nonlinearity-by-resiliency joint table claimed here. The record already excludes those isolated classical/extremal facts from its novelty claim.

## Scientific value
Status: **PASS**.

A complete small-parameter joint classification across two standard cryptographic invariants is a natural reference computation. The n=4 full space is the last tiny full Boolean-function universe before the 2^32 n=5 wall, and the complete n=5 cyclic-symmetry slice is a literature-natural restriction; the tables provide more than isolated extrema.

## Limitations and residual risk
- The n=5 statement concerns only the 256 cyclic-rotation-symmetric functions, not all 2^32 five-variable Boolean functions.
- Several extremal counts/properties are already present in earlier RSBF literature; the originality claim is restricted to the complete joint frequency tables.
- Residual risk remains that raw data behind older exhaustive searches may contain unpublished equivalent counts.
- The 2008 authors' underlying exhaustive computation may contain unpublished/raw joint counts; originality here is only for the published-table comparison.
