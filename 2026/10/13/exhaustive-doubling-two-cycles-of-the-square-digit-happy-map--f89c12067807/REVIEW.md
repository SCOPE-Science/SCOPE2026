# Independent mathematical audit

## correctness

PASS

For X=ab+c with 1<=a<b and 0<=c<b, no carry when doubling forces S_b(2X)=4 S_b(X)=8X, contradicting S_b(2X)=X. With a required carry, 2X has digits (2a+1,2c-b) and the exact two cycle equations have c-resultant (b^2+1)(5a-b+3)(13a-b+5). The b=13a+5 branch yields c=5a+2 and violates 2c>=b. The surviving b=5a+3 branch gives c=3a+2; its digits obey all two-digit bounds, and substitution proves the converse for every a>=1. Independent SymPy resultant and direct bases 2..130 match. No finite search is the infinite proof.

## originality

PASS

The closest 2025 primary paper explicitly constructs b=5t+3 and X=(t,3t+2)_b with Y=2X. A construction is not the all-base converse under both-digit and ratio-two constraints. The elimination argument supplies the unique necessary branch. Older happy-function cycle literature and OEIS tables cover other questions; incomplete access to Hargreaves–Siksek 2010 leaves a real priority risk.

## value

PASS

The 2025 source singled out the doubling two-cycle family; identifying precisely when it is exhaustive is a motivated minimal-digit rigidity problem. The forced carry and rejected algebraic branch explain exactly why no other two-digit ratio-two patterns exist. Not a mere additional numerical example or an arbitrary base cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
