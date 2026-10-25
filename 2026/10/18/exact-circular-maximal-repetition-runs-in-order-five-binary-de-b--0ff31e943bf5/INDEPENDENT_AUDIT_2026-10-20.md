# Independent mathematical audit

## correctness

PASS

A run is the cyclic interval triple (start,length,least period) with 2p≤length≤32 and strict one-symbol nonextension both sides. Repeated n-bit windows prohibit a periodic factor of length ≥p+n, hence 2p≤L≤p+4 implies p≤4 and L≤8, so no omitted longer periodic intervals. Built a separate complete enumeration of all 65,536 local incoming/outgoing pairings in the order-four de Bruijn digraph, retained precisely 2048 single 32-edge Euler tours, and independently scanned every start and length 2..8 for least periods and both boundary inequalities. Reproduced r1=8,r2=2 for each cycle, all six joint frequency cells and the distribution of 12/13/14 runs, rather than relying only on packaged VERIFY_OK or profiles.csv. The Euler pairing bijection covers every rotation class uniquely via marked edge 00000. Orbit-cell splits and CSV row-by-row checks were examined in the source program but not independently rerun, so these secondary symmetry numbers have less independent computational confirmation; source source-code derivation and group action were checked.

## originality

PASS

Crochemore et al. and Bannai et al. treat generic linear-string run bounds and structural characterization; fixed-weight de Bruijn constructions give existence of cycles, while already known uniform factor counts account for unary runs. None of the inspected statements implies the specific full six-cell frequency law for all 2048 order-five circles or reversal/complement symmetry classes. Searches for de Bruijn run spectra and circular periodicity found only adjacent, not covering, results.

## value

PASS

All de Bruijn order-five rotation classes form a canonical finite family. Their exact joint maximal periodicity profile, sharp attainable run counts, moments, and symmetry reduction are natural reproducible invariants that a subsequent researcher could use as finite benchmark; finite size is intrinsically complete and not an arbitrary subcollection. Background r1 and r2 alone are not the claimed contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
