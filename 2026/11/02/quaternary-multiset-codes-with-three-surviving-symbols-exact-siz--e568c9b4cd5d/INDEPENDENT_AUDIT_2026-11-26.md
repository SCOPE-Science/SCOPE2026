# Independent mathematical audit

## correctness

PASS

For the repaired claim, a common deletion output of size three exists exactly when the sum of the coordinatewise minima is at least three; a larger common output can be shortened. Each coordinate can be heavy (multiplicity at least three) for at most one codeword. Hence four heavy words in an optimizer use all coordinates once. At n=5 the only compatible exceptional pairs have disjoint doubled coordinates and each member's single copy lies in the opposite doubled pair. These give 12 labelled pairs; for the displayed normal form the constraints are u,z=0..2 with u+z<=2, and v,w=0..1, so 24 independent heavy completions per pair. At n=6, with exceptional type (2,2,2,0), a heavy word on a doubled coordinate can only place extras on the zero coordinate d. The word heavy at d places at most two extras total on the other three coordinates; the constraints u_i+y_i<=2 give 144 completions and four choices of d. With type (2,2,1,1), the doubled coordinates force constants; each other heavy coordinate has five choices, and exactly the three mutually directed cross-extra pairs of total size greater than two are incompatible, giving six times 22. At n=7 the exceptional word has one singly occupied coordinate, and only its heavy word can have one extra copy; n=8 leaves only the four constants and the all-twos word. The known sizes used here follow from the same heavy bound and the stated exceptional cases; for n>=9 every word is heavy, so four constants attain the optimum without any optimizer-count assertion. The finite lexicographic recursion maintains pairwise compatibility and uniquely enumerates sets, not orderings. A fresh bounded check with a dynamic optimum reproduced the four maxima (6,5,5,5), labelled counts (288,708,16,1), all four rows of Burnside fixed counts, and orbit counts (14,46,2,1), using both canonical images and Burnside averaging over S4. The corrected files preserve those claims and the usable verification front matter; bit_count requires Python 3.10 or newer. The frozen verifier was inspected, not executed.

## originality

PASS

Credit is restricted to the complete labelled and alphabet-orbit census through the last length admitting size five, including the unique optimiser at eight. The original capacity claim is materially covered and is now explicitly identified as known. The strongest adjacent catalogue and primary results concern optimum sizes or coarse structure, not the compatibility of all heavy-word completions and their stabilizers. No exact census match was found in the inspected sources.

## value

PASS

The range is the full exceptional span from length five to the last length supporting more than four codewords. Counting optimal codebooks before and after relabelling answers an identifiable design question: how many genuinely different optimal choices are available, and where does rigidity set in? The census shows a collapse from hundreds of labelled choices to a single codebook, with nontrivial class counts in the intermediate cases. It pairs a structural completion argument with complete finite enumeration, not just a recomputation of known capacity or an arbitrary sample of short lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
