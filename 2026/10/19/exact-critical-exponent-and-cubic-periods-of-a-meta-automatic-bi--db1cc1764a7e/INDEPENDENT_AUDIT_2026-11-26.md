# Independent mathematical audit

## correctness

PASS

The displayed morphism is prolongable on 0, reaches all letters, and creates exactly the adjacent pairs obtained by closing the internal pairs under image boundaries. Every length-L factor fits inside two image blocks of length 4^k≥L, and every such image of an occurring adjacent pair appears at an aligned boundary. Thus the exact enumeration and its residues modulo 4 describe the infinite language. Independently reproduced: 10 adjacent pairs, 100 state factors of length 15 and 186 binary factors of length 29 with unique phases, 1,301 factor checks excluding state overlaps for p=1..13, and 592 binary length-85 factors giving maxima (2,10,6,10,10,26,14,18,17,18,18,26,20,36). For a hypothetical state overlap of smallest period p≥14, equal length-15 windows at offsets 0,p force p=4q. Comparing first letters of images for the next q aligned blocks and, if the first image is partial, its last letter, produces a state overlap of period q; both the first-letter and last-letter maps are injective. In a binary cube with p≥15, 29-symbol windows fit at offsets 0,p and similarly give p=4q≥16. The four coded images are distinct. The complete aligned blocks therefore give period q on 3q state symbols if the first block is complete, or 3q−1 if it is partial; both lengths are at least 2q+1. This contradicts overlap-freeness. The length-85 census then captures all shorter periodic factors (extend right to length 85), and no periodic factor of length at least 85 for p≤14 can escape because its initial 85 letters would contradict the listed maxima. Only p=2,6 reach 3p, and their maximal lengths are 10 and 26. Exponent uses least period: any factor exceeding exponent 5 would contain a cube of its least period, impossible by those maxima. The alternating factor at index 2 has least period 2 and length 10.

## originality

PASS

The word, coding and study of its factor complexity are known; general computability of its critical exponent is also known. The supported distinct result is the specific exponent and complete list of cube periods with exact maximal lengths. No equivalent statement was found in the inspected work and ranked catalogue results.

## value

PASS

M1 is a specific word introduced independently in the study of meta-automatic recurrences, and critical exponent is a canonical measure of repetition for such words. The exact answer and short list of allowable cube periods settle more than whether repetitions exist: they distinguish the repeated patterns left by a noninjective coding from the overlap-free state sequence. This gives a concrete, reusable exact repetition profile for comparison with other automatic words and a human-checkable reason no large periods survive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
