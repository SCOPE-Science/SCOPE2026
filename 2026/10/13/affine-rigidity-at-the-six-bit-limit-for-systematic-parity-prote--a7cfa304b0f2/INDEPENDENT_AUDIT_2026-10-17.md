# Independent mathematical audit

## correctness

PASS

The two-distance requirement is d_H((x,p(x)),(y,p(y)))>=3 for all distinct x,y and >=5 for opposite message parity. For a one-coordinate flip, the check-word difference must have weight >=4; when r=4 each edge forces the unique all-ones difference and two-coordinate flips violate data-distance three, so r>=5 at k>=2. At r=5 the k neighbors around any x have distinct check images among only six words in the radius-one ball around complement p(x), forcing k<=6. For k=6 all six edge increments are J and J+e_j, one of each at every vertex. The square XOR identity and distinct adjoining edge colors force opposite edges equal, so each coordinate direction's increment is constant: p(x)=b+sum_i x_i(J+e_{pi(i)}) with pi a permutation. All such maps satisfy the distances by checking message-weight cases 1,2,3 and >=4, and the map b/pi is injective, yielding 2^5*6!=23040. Independent finite enumeration confirmed all 30 possible admissible square colorings and the 720 zero-offset permutations; it is not substituted for the proof over the full hypercube. Cases k=1 (four checks), 2..6 (five), and k>=7 (>five) are kept separate.

## originality

PASS

The general redundancy bound of Rajput et al. is prior art and gives r>=5; the four-bit parity construction is also known. The older linear separation-vector feasibility result (van Gils, 1982) means six-bit linear existence is not novel. The claim that all arbitrary nonlinear systematic maps at the saturated six-direction boundary necessarily become affine, with 23040 labeled maps, is not implied by those bounds/existence results in the inspected primary text. Best-of-knowledge novelty only, with unindexed nonlinear unequal-protection work retained as a risk.

## value

PASS

At the known minimum five-bit redundancy, the maximum systematic message dimension and all boundary maps form a natural rigidity and encoder-design question. The result rules out any nonlinear equality alternatives instead of only giving one code; the enumeration is a structural consequence, not a random small search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
