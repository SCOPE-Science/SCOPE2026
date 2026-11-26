# Independent mathematical audit

## correctness

PASS

Each admissible input block extends bi-infinitely by zeros, so the 13 local values determine distinct maps and all 21 tests for two adjacent 1 outputs are necessary and sufficient. In the labeled graph on admissible four-blocks, a path corresponds to an overlapping legal input block, and conversely; hence its label appears in the image exactly when the endpoint subset is nonempty. The subset and last bit capture both continuation constraints. Breadth-first closure is exact at all lengths, and equality of finite languages implies equality of the two-sided shifts by compactness and shift invariance. Independent enumeration reproduces the 229 maps, 11 onto codes, 5 shifts, all six periodic collisions, every shortest-omission count and all 229 exact classification.csv rows. The unique mask with shortest omission of length 21 is 4132. Separately generating all 196418 legal length-25 inputs produces 28655 of 28657 legal length-21 words, with precisely the two stated reverse omissions and the complete length-20 prefix language. Radius one gives 7 self-maps and only the three shifts onto; radius zero has only identity onto. Thus both finiteness of the search and the extension to the infinite system are justified.

## originality

PASS

The de Bruijn/predecessor presentation and subset closure are standard methods. The distinct result is the complete constrained-radius census, the first radius with a proper onto map, and the exact shortest-omission maximum with its unique rule and two defects. The nearest indexed claim is materially related but starts at two required zeros between ones; its counts and rigidity statements do not cover the one-required-zero golden-mean shift. None of the inspected general or exact classification results supplies the frozen figures and threshold.

## value

PASS

The golden-mean shift is a canonical constrained binary system. The census resolves the minimum centered radius at which information can be lost by a surjective rule, and gives the exact observation length sufficient to distinguish every strict image by its block language. The unique rule whose language first differs at length 21 is a useful concrete test case for short-neighborhood surjectivity algorithms, not an arbitrary slice of a larger enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
